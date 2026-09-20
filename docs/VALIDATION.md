# 候选包验证报告

## 2026-09-20 命名与补充材料候选更新

当前版本为0.1.1-public-candidate。完成6个Skill入口格式检查、10个JSONL共398行解析、
21个原始补充文件逐字节复制校验，并重新生成安装ZIP与仓库CHECKSUMS。
这些检查不构成生物学准确率评测，也没有重新执行历史科学回归或真实客户端安装测试。
当前运行结果见根目录VALIDATION-RESULTS.json。

以下为0.1.0历史验证记录，保留作版本历史；其中数量不是当前补充包数量，
研究者姓名表示历史内部来源标识，非人工专家参与或确认。

## 验证范围

验证对象为 `skills/mirna-five-lens-panel` 及其五个内嵌 Lens，不包含原项目研究缓存、原始评测工作区或权威 `release/` 目录。

## 结构检查

- 顶层面板存在合法 `SKILL.md` frontmatter；
- 五个内嵌 Lens 均存在 `SKILL.md`；
- `references/lens-registry.md` 与五个内嵌目录一致；
- 面板不依赖包外相对路径；
- Jin 的状态和输出契约保留 `supervised_preview`。

## 数据与版权检查

- 允许文件类型：Markdown、YAML、JSONL；
- 不包含 PDF、论文全文、FASTQ/BAM/SRA、模型权重、可执行文件、凭据或缓存；
- source manifest 保存书目元数据和合法 URL；
- Evidence Card 保存结构化转述和证据边界，不重新分发论文全文。

## 科学状态

- Axtell、Chen、Meyers、Carrington：`validated`；
- Jin：`supervised_preview`，权威来源状态仍为 `needs_review`；
- Bartel、Evidence Auditor 和原 Router 不包含在面板中。

## 生成后验证

候选包生成脚本会重新执行：

1. 所有 Skill 的 `quick_validate`；
2. 所有 JSONL 行解析；
3. 相对引用路径闭包检查；
4. 禁止文件类型和敏感字符串扫描；
5. ZIP 结构与解压测试；
6. SHA-256 生成和复核；
7. 临时 WorkBuddy 用户目录安装烟雾测试。

最终机器可读结果保存在 `VALIDATION-RESULTS.json`。如果该文件中的 `overall` 不是 `PASS`，不应上传 GitHub Release。

## 本次候选结果

- Skill Creator `quick_validate`：面板 1/1 PASS，内嵌 Lens 5/5 PASS；
- JSONL：10 个文件、398 条记录全部可解析；
- 本地 Markdown 链接缺失：0；
- 禁止文件：0；
- 私钥材料命中：0；
- ZIP：88 个成员，CRC/结构检查 PASS；
- 短路径模拟用户 Skills 目录解压：入口存在、5 个内嵌 Lens、88 个文件、0 个脚本；
- 校验和：103 条生成并复核通过；
- 远程推送：未执行；
- 原项目权威发布状态：未改变。
