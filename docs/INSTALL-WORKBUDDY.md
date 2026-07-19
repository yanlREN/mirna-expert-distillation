# WorkBuddy 安装教程

## 安装前

- 建议使用当前可用的 WorkBuddy 稳定版；
- 下载 GitHub Release 中的 `mirna-five-lens-panel-workbuddy.zip`；
- 同时下载或查看仓库根目录的 `CHECKSUMS.sha256`；
- 这是第三方科研 Skill，首次使用建议选择 Ask / 问一问模式。

WorkBuddy 官方技能页面说明，“添加技能”支持通过“上传技能”导入本地技能包，导入后系统自动配置；官方同时建议安装第三方 Skill 前核验来源、权限和脚本内容：

https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market

## 方法一：界面上传 ZIP

1. 打开 WorkBuddy。
2. 进入“技能”。
3. 切换到“已安装”。
4. 点击“添加技能”。
5. 选择“上传技能”。
6. 拖入或选择 `mirna-five-lens-panel-workbuddy.zip`。
7. 等待 WorkBuddy 完成导入。
8. 在“已安装”中搜索 `mirna-five-lens-panel`，确认已启用。
9. 新建任务，在输入区选择该 Skill。

不要同时启用五个内嵌 Lens 的重复副本。面板已经包含全部五个 Lens，只选一个面板即可。

## 方法二：从 GitHub 源码手动安装

如果 WorkBuddy 版本不接受 ZIP，可下载仓库源码并复制 Skill 目录。

### Windows

复制：

```text
<下载目录>\skills\mirna-five-lens-panel
```

到：

```text
C:\Users\<你的用户名>\.workbuddy\skills\mirna-five-lens-panel
```

最终应存在：

```text
C:\Users\<你的用户名>\.workbuddy\skills\mirna-five-lens-panel\SKILL.md
```

### macOS/Linux

复制：

```text
<下载目录>/skills/mirna-five-lens-panel
```

到：

```text
~/.workbuddy/skills/mirna-five-lens-panel
```

最终应存在：

```text
~/.workbuddy/skills/mirna-five-lens-panel/SKILL.md
```

若你的 WorkBuddy 显示了不同的用户级技能目录，应以界面显示为准。

## 启用和首次测试

1. 完全退出并重新打开 WorkBuddy，或等待 Skills 热加载完成。
2. 新建任务。
3. 选择 Ask / 问一问模式。
4. 在技能选择器中启用 `mirna-five-lens-panel`。
5. 输入：

```text
请用五视角面板分析：只有数据库收录和预测发卡，能否确认一个植物候选为 miRNA？
请显示五个 Lens 的状态，并保留 Jin 的 supervised_preview 标签。
```

预期表现：

- 输出 Axtell、Chen、Meyers、Carrington、Jin 五个部分；
- 前四个显示 `validated`；
- Jin 显示 `supervised_preview` 和证据截止日期；
- 不把数据库收录或预测发卡写成确认 miRNA；
- 最后包含共同点、分歧、证据缺口和下一步问题。

## 更新

1. 先关闭或卸载旧版面板。
2. 下载新版本 ZIP 并核对校验和。
3. 重新上传，或用新目录覆盖旧目录。
4. 重启 WorkBuddy。
5. 重新运行首次测试，确认状态标签和版本说明正确。

不要只替换 `SKILL.md`；内嵌 Lens 和 references 必须保持同一版本。

## 卸载

在 WorkBuddy“技能”→“已安装”中选择卸载；若使用手动安装，则在 WorkBuddy 完全退出后删除用户级 Skills 目录中的 `mirna-five-lens-panel` 文件夹。

## 常见问题

### 搜索不到 Skill

- 确认不是多套了一层目录；`mirna-five-lens-panel/SKILL.md` 应直接存在。
- 完全退出 WorkBuddy 后重新打开。
- 检查 `SKILL.md` 文件名和大小写。
- 使用界面“上传技能”重试。

### 只出现统一答案，没有五个部分

- 明确选择 `mirna-five-lens-panel`。
- 在问题中写明“分别输出五个 Lens”。
- 确认安装包完整，尤其是 `references/lenses/`。

### Jin 没有 supervised_preview 标签

停止使用该输出并重新安装完整候选包。缺少这个标签意味着包被错误修改或 Skill 没有按契约执行。

### 是否需要本地大模型或原始测序数据

不需要。本 Skill 只提供结构化分析规则和证据摘要；实际推理由 WorkBuddy 所选模型完成。它不执行 small RNA-seq/PARE 重分析，也不下载 FASTQ、BAM 或 SRA 数据。
