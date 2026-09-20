#!/usr/bin/env python3
"""Deterministic offline Codex/Luna coordinator sample for the isolated release.

This never calls an external model and never reads BASE decision text.  It
checks the prescribed sample strata against the frozen incremental source.
"""
from __future__ import annotations
import argparse, hashlib, json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

QA_KEYS=("qa_id","paper_id","section_type","section_id","qa_type","question","answer","evidence_sentence","expert_skill_used","expert_skill_name","expert_skill_path","expert_skill_version","expert_skill_source_sha256","expert_skill_release_status","expert_skill_output_id","expert_information_point_id","expert_skill_status","expert_usage","generator_model","self_check","review_model","review_model_id","review_status","review_reason","final_adjudicator","final_status")

def load(path):
    rows=[]
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip(): rows.append(json.loads(line))
    return rows

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--base",type=Path,required=True); ap.add_argument("--report",type=Path,required=True); ap.add_argument("--qc",type=Path,required=True); args=ap.parse_args()
    source={r["task_id"]:r for r in load(args.base/"input/incremental_task_input_v1.jsonl")}
    terms=load(args.base/"results/incremental_terminal_records_v1.jsonl"); qa=load(args.base/"results/qa_incremental_v1.jsonl")
    by_task={}
    for r in qa: by_task.setdefault(r["qa_id"].split("::QA",1)[0],[]).append(r)
    candidates=[]
    for tid,t in sorted(source.items(),key=lambda x:x[1]["input_order"]):
        rows=by_task.get(tid,[])
        if not rows: continue
        digest=int(hashlib.sha256(tid.encode()).hexdigest()[:8],16)
        if digest%50==0 or any(r.get("qa_type")=="RELATION_FACT" and digest%20==0 for r in rows) or any(r.get("qa_type")=="EVIDENCE" and digest%20==0 for r in rows):
            candidates.append((tid,t,rows))
    checks=[]; errors=[]
    for tid,t,rows in candidates:
        for r in rows:
            ok=tuple(r.keys())==QA_KEYS and r.get("paper_id")==t["paper_id"] and r.get("section_id")==t["section_id"] and r.get("section_type")==t["section"] and isinstance(r.get("evidence_sentence"),str) and r["evidence_sentence"] in t["section_text"] and r.get("review_status")=="PASS" and r.get("final_status")=="PASS"
            checks.append(ok)
            if not ok: errors.append({"task_id":tid,"qa_id":r.get("qa_id"),"reason":"schema_identity_evidence_or_status"})
    terminal_states=Counter(r.get("terminal_state") for r in terms)
    result={"protocol_id":"MIRNA_QA_V4FLASH_COVERAGE_COMPLETION_V1","adjudicator":"CODEX_LUNA_MAX_OFFLINE_COORDINATOR","api_request_count":0,"sample_tasks":len(candidates),"sample_qa_records":len(checks),"sample_pass":sum(checks),"sample_fail":len(errors),"sample_pass_rate":(sum(checks)/len(checks) if checks else 1.0),"terminal_states":dict(terminal_states),"errors":errors,"timestamp_utc":datetime.now(timezone.utc).isoformat()}
    args.qc.parent.mkdir(parents=True,exist_ok=True); args.qc.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
    args.report.parent.mkdir(parents=True,exist_ok=True); args.report.write_text("# Codex/Luna Max offline sample\n\n"+"\n".join([f"- Protocol: `{result['protocol_id']}`",f"- Sample tasks: {len(candidates)}",f"- Sample QA records: {len(checks)}",f"- Pass rate: {result['sample_pass_rate']:.4f}","- API requests: 0","- Evidence, identity, schema and status checks were run against the frozen incremental input."])+"\n",encoding="utf-8",newline="\n")
    print(json.dumps(result,ensure_ascii=False,sort_keys=True)); return 0 if not errors else 1
if __name__=="__main__": raise SystemExit(main())
