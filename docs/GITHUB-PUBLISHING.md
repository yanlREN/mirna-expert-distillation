# GitHub 发布操作说明

本目录已经按一个独立仓库根目录组织，但当前项目不会自动创建仓库或推送远程。发布者应先人工检查所有文件。

## 发布前检查

1. 阅读 `README.md`、`NOTICE.md` 和 `RELEASE-MANIFEST.yaml`。
2. 确认 Jin 始终为 `supervised_preview`。
3. 确认 `dist/mirna-five-lens-panel-workbuddy.zip` 存在。
4. 重新核对 `CHECKSUMS.sha256`。
5. 确认没有 PDF、FASTQ/BAM/SRA、模型权重、缓存、日志、凭据或私人资料。
6. 确认仓库描述没有“专家本人”“官方背书”或“五位都已验证”等表述。

## 通过 GitHub 网页发布

1. 在 GitHub 新建一个空仓库，例如 `mirna-five-lens-workbuddy`。
2. 不要自动添加另一个 README、LICENSE 或 `.gitignore`，因为本目录已提供。
3. 使用 GitHub 网页的 Upload files 上传本目录全部内容。
4. 检查目录层级，确保仓库根目录直接看到 `README.md` 和 `skills/`。
5. 创建或更新 Release，本次候选版标签可用 `v0.1.1-public-candidate`。
6. 勾选 **Set as a pre-release**。
7. 上传 `dist/mirna-five-lens-panel-workbuddy.zip` 和 `CHECKSUMS.sha256` 作为附件。
8. 在 Release 说明中再次写明“四个 validated + Jin supervised_preview”。

## 仓库建议设置

- 开启 Issues，用于报告科学错误、失效链接和安装问题；
- 开启分支保护，要求科学结论变更经过审阅；
- 不启用会自动抓取论文全文或原始测序数据的工作流；
- 对第三方 PR 检查新增二进制文件、凭据和超大文件；
- 在 About 中使用“framework-based research analysis; not expert endorsement”。

## 后续正式版条件

如果要把版本从 public candidate 升级为正式五视角发布，至少应在新的独立 run 中修复并回归 JIN-A03、JIN-A04、JIN-A06、JIN-S01，重新验证引用和证据截止，并确认所有五个 Lens 为 A 级且零硬失败、零未解决发布回退。
