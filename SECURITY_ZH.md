# Security

[中文](SECURITY_ZH.md) | [English](SECURITY.md)

## Package capabilities

可安装的Skill ZIP只包含Markdown、YAML和JSONL文件，不包含脚本、可执行程序、网络连接器、自动文件写入逻辑或账户凭据。它本身不会下载数据、调用第三方API或训练模型。

仓库的`methods-and-qc/reference-code/`包含历史质量检查参考代码，但它们不在可安装Skill ZIP中，也不会在安装Skill时自动运行。

WorkBuddy 运行时使用的模型、网络、日志和权限由用户的 WorkBuddy 配置决定，不由本仓库控制。

## 安装前检查

1. 从可信仓库或 GitHub Release 下载。
2. 使用 `CHECKSUMS.sha256` 核对 ZIP 和 Skill 文件。
3. 解压检查仅包含预期的 `.md`、`.yaml` 和 `.jsonl` 文件。
4. 检查 `SKILL.md` 是否仍明确禁止冒充专家，并保留专家视角5的 `supervised_preview` 状态。
5. 首次在 Ask / 问一问模式中使用，不授予不必要的文件或系统权限。

## 数据隐私

不要向未知模型服务提交患者身份信息、未公开实验数据、密码、API 密钥、机构订阅凭据、受限论文全文或其他敏感材料。若需要分析未公开科研内容，应先确认 WorkBuddy 所选模型和组织政策允许相应数据处理。

## 报告问题

提交安全问题时，请说明：包版本、文件哈希、WorkBuddy 版本、复现步骤、实际行为和预期行为。不要在公开 Issue 中粘贴凭据、私人数据或受版权保护全文。
