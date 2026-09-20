#!/usr/bin/env python3
"""Strict validator for one isolated incremental worker staging directory."""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path
from typing import Any
KEYS=("qa_id","paper_id","section_type","section_id","qa_type","question","answer","evidence_sentence",
"expert_skill_used","expert_skill_name","expert_skill_path","expert_skill_version","expert_skill_source_sha256",
"expert_skill_release_status","expert_skill_output_id","expert_information_point_id","expert_skill_status",
"expert_usage","generator_model","self_check","review_model","review_model_id","review_status","review_reason",
"final_adjudicator","final_status")
QA_TYPES={"RELATION_FACT","EVIDENCE","CONTEXT","RESULT_PHENOTYPE","CONCLUSION_SIGNIFICANCE"}
SECTIONS={"introduction","results","discussion","conclusion"}
TERMINAL={"ACCEPTED_QA","NO_VALID_QA_AFTER_REVIEW","SOURCE_INVALID","GENERATION_FAILED_EXHAUSTED","EXCLUDED_WITH_DOCUMENTED_REASON"}
def sha(b:bytes)->str:return hashlib.sha256(b).hexdigest()
def load(path:Path):
 if not path.exists(): return []
 rows=[]
 with path.open("r",encoding="utf-8") as fh:
  for line in fh:
   if line.strip(): rows.append(json.loads(line))
 return rows
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--input",type=Path,required=True); ap.add_argument("--worker-root",type=Path,required=True); ap.add_argument("--qc",type=Path,required=True); args=ap.parse_args()
 tasks=load(args.input); by_id={x["task_id"]:x for x in tasks}
 terms=load(args.worker_root/"terminal_records.jsonl"); qas=load(args.worker_root/"accepted_records.jsonl")
 if len(by_id)!=len(tasks) or len(terms)!=len(tasks): raise RuntimeError("task/terminal count failure")
 tids=[x["task_id"] for x in terms]
 if len(set(tids))!=len(tids) or set(tids)!=set(by_id): raise RuntimeError("terminal task coverage/uniqueness failure")
 seen=set()
 for row in qas:
  if tuple(row.keys())!=KEYS: raise RuntimeError("exact 27-field schema/order failure")
  if row["qa_id"] in seen: raise RuntimeError("duplicate qa_id")
  seen.add(row["qa_id"]); m=re.match(r"^(.+)::QA[0-9]{2}::[0-9a-f]{24}$",row["qa_id"])
  if not m or m.group(1) not in by_id: raise RuntimeError("qa identity envelope failure")
  src=by_id[m.group(1)]
  if row["paper_id"]!=src["paper_id"] or row["section_type"]!=src["section"] or row["section_id"]!=src["section_id"]: raise RuntimeError("frozen identity mismatch")
  if row["section_type"] not in SECTIONS or row["qa_type"] not in QA_TYPES: raise RuntimeError("enum failure")
  for k in ("question","answer","evidence_sentence","review_reason","expert_skill_output_id","expert_information_point_id"):
   if not isinstance(row[k],str) or not row[k].strip(): raise RuntimeError(f"empty {k}")
  if row["evidence_sentence"] not in src["section_text"]: raise RuntimeError("evidence not source substring")
  if row["expert_skill_used"] is not True or row["expert_skill_name"]!="nuwa_mirna_expert" or row["expert_skill_status"]!="SUCCESS": raise RuntimeError("Nuwa provenance failure")
  if row["expert_skill_version"]!="0.1.0-public-candidate" or row["expert_skill_source_sha256"]!="300c29a3600cd3b5e882a3bff96b593b64df69c2b59a66e14579c0310c13ef71": raise RuntimeError("Nuwa version/SHA failure")
  if row["generator_model"]!="deepseek-v4-flash" or row["review_model"]!="deepseek-v4-flash" or row["review_model_id"]!="deepseek-v4-flash": raise RuntimeError("model identity failure")
  if row["review_status"]!="PASS" or row["final_status"]!="PASS": raise RuntimeError("final status failure")
 by_task={}
 for row in qas: by_task[row["qa_id"].split("::QA",1)[0]]=by_task.get(row["qa_id"].split("::QA",1)[0],0)+1
 for t in terms:
  if t["terminal_state"] not in TERMINAL: raise RuntimeError("invalid terminal state")
  if t["qa_count"] != by_task.get(t["task_id"],0): raise RuntimeError("terminal QA count mismatch")
  if t["terminal_state"]=="ACCEPTED_QA" and t["qa_count"]<1: raise RuntimeError("accepted terminal without QA")
  if t["terminal_state"]!="ACCEPTED_QA" and t["qa_count"]!=0: raise RuntimeError("nonaccepted terminal with QA")
 qc={"status":"PASS","input_tasks":len(tasks),"terminal_tasks":len(terms),"accepted_records":len(qas),
 "unique_qa_id":len(seen),"terminal_counts":{s:sum(1 for t in terms if t["terminal_state"]==s) for s in sorted(TERMINAL)},
 "output_sha256":sha((args.worker_root/"accepted_records.jsonl").read_bytes()),"terminal_sha256":sha((args.worker_root/"terminal_records.jsonl").read_bytes())}
 args.qc.parent.mkdir(parents=True,exist_ok=True); args.qc.write_text(json.dumps(qc,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n"); print(json.dumps(qc,ensure_ascii=False,sort_keys=True))
if __name__=="__main__":main()
