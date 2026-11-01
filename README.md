# anything-to-learn

**不想听课？把课件丢给它，按考试要的学。**

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg) ![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-blue.svg) ![Version](https://img.shields.io/badge/version-0.2-orange.svg) ![Platforms](https://img.shields.io/badge/works%20with-Claude%20%C2%B7%20Codex%20%C2%B7%20Gemini%20CLI%20%C2%B7%20Cursor%20%C2%B7%20Copilot%20%C2%B7%20OpenCode-8A2BE2.svg)

anything-to-learn 是一个面向自主学习者的 Agent Skill。它把讲义、PPT、截图、板书照片、视频字幕、代码仓库乃至往年试卷整理成**可溯源的学习材料**，再以考试目标为约束，按你的节奏一对一教学。它记得你学到哪、哪里没懂，但不布置作业，也不推送复习计划。

*A low-pressure, exam-aware self-study tutor skill. Any course material in, adaptive one-on-one learning out, progress carried across sessions. Works with any agent that supports the open Agent Skills format.*

```text
你：下周三期中考，范围第 2–5 讲，这是前两年的卷子和第 3 讲的 PPT。

它：我从 3 个文件里读到 41 个知识点（第 3 讲 PPT 第 7 页的公式没看清，请确认）。
    两份卷子里，推导题占 35%，每道都以"解释结果"收尾。
    按"每分钟能换多少分"，建议先做：
      1. KV cache 显存计算（10 分，约 25 分钟）
      2. 推导后的结果解释（每题 2–4 分，约 10 分钟）
    位置编码变体近两年 0 分，这次放最后。要从第 1 项开始吗？
```

<sub>以上为示意对话，展示的是 skill 的设计行为。</sub>

---

## 目录

- [它和其他工具有什么不同](#它和其他工具有什么不同)
- [安装](#安装)
- [开始第一次学习](#开始第一次学习)
- [工作原理](#工作原理)
- [学习科学依据](#学习科学依据)
- [它不会做的事](#它不会做的事)
- [项目结构](#项目结构)
- [状态与路线图](#状态与路线图)

## 它和其他工具有什么不同

"把资料变成课和题"的工具已经很多。anything-to-learn 把力气花在五件事上：

| 功能 | 做什么 |
|---|---|
| **应试反推** | 从往年题、作业、老师划的重点出发，分析题型占比、考点分值和常见套路，按"每分钟换多少分"排学习顺序；练习题与真题同题型、同符号，并标注仿照的是哪一题 |
| **误解地图** | 记录"自信地错"背后的错误信念，先确认再纠正，并在它会连带影响的知识点之前先检查 |
| **在你的代码里学** | 读你的作业仓库，就你自己写的代码提问；先预测再运行，用测试判对错；报错时带你排查，不替你改 |
| **反向讲授** | 你来讲，它扮演一个缺课但很聪明的同学，追问关键步骤、抛出常见误解 |
| **处处可溯源** | 每个知识点标注出处（第几页 / 第几张幻灯片 / 第几分钟），它补充的内容单独标出 |

同时，它保留了有研究支持的学习方法，但去掉了课堂式的压力：

| | 课堂式 AI tutor | anything-to-learn |
|---|---|---|
| 把握程度 | 每题手动标"确定 / 大概 / 猜" | 从作答的语气和推理里自动判断 |
| 复习 | 推送复习日程 | 没有日程；每次开场 1–2 道热身题，自动挑薄弱点 |
| 卡住时 | 不先做就不给答案 | 五级提示阶梯，随时可以要答案，只记录不拒绝 |
| 教法 | 每课都要你先尝试 | 新手先看例题，有基础再先尝试 |
| 课程 | 一次性生成整门课 | 先出学习地图，课时按进度即时生成 |
| 考试 | 整门课平均用力 | 按往年题反推重点和顺序 |
| 错题 | 记对错 | 记错误想法和它会影响的知识点 |

## 安装

### 前置条件

- 一个支持 [Agent Skills](https://agentskills.io) 格式的 AI 助手或 agent（见下表），或任意能设置自定义指令的聊天产品。
- 用命令行安装时需要 Git；用一键安装时需要 Node.js（`npx`）。
- skill 本身是纯 Markdown：没有脚本、没有依赖、不需要 API key 或联网。

### 平台速查

| 平台 | 用户级目录（所有项目可用） | 项目级目录 | 备注 |
|---|---|---|---|
| Claude（网页 / 桌面 / 手机） | 设置页上传 zip | — | Pro / Max / Team / Enterprise |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` | |
| OpenAI Codex CLI | `~/.agents/skills/` | `.agents/skills/` | |
| Gemini CLI | `~/.gemini/skills/` 或 `~/.agents/skills/` | `.gemini/skills/` 或 `.agents/skills/` | 也可用 `gemini skills install` |
| Cursor | `~/.cursor/skills/` 或 `~/.agents/skills/` | `.cursor/skills/` 或 `.agents/skills/` | 也读取 `~/.claude/skills/` |
| VS Code + GitHub Copilot | `~/.copilot/skills/` | `.github/skills/` | 本地会话也读取 `.agents/skills/` |
| OpenCode | `~/.config/opencode/skills/` | `.opencode/skills/` | 也读取 `.claude/skills/`、`.agents/skills/` |
| ChatGPT、DeepSeek、Kimi、豆包等 | 不支持 skill 文件夹 | — | 用[复制粘贴方式](#不支持-skill-的聊天产品) |

> **一个目录覆盖多数工具**：`~/.agents/skills/` 会被 Codex CLI、Gemini CLI、Cursor、OpenCode 和 Copilot 本地会话读取。装在这里，再给 Claude Code 建一个软链接即可（见[通用安装](#通用安装推荐)）。

### 一键安装（skills CLI）

第三方工具 [skills](https://github.com/vercel-labs/skills) 能自动识别你装了哪些 agent，并安装到对应目录：

```bash
# 装到所有检测到的 agent（用户级）
npx skills add Looffeeuu/anything-to-learn -g

# 只装到指定 agent
npx skills add Looffeeuu/anything-to-learn -g -a claude-code -a codex -a cursor
```

### 通用安装（推荐）

```bash
# 1. 装到通用目录（Codex / Gemini CLI / Cursor / OpenCode / Copilot 都能读到）
git clone https://github.com/Looffeeuu/anything-to-learn.git ~/.agents/skills/anything-to-learn

# 2. 让 Claude Code 也能读到
mkdir -p ~/.claude/skills
ln -s ~/.agents/skills/anything-to-learn ~/.claude/skills/anything-to-learn
```

Windows（PowerShell）：

```powershell
git clone https://github.com/Looffeeuu/anything-to-learn.git "$env:USERPROFILE\.agents\skills\anything-to-learn"
New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\anything-to-learn" -Target "$env:USERPROFILE\.agents\skills\anything-to-learn"
```

### 按平台安装

<details>
<summary><b>Claude（网页 / 桌面 / 手机）</b></summary>

1. 下载并打包（zip 内的文件夹名必须是 `anything-to-learn`）：
   ```bash
   git clone https://github.com/Looffeeuu/anything-to-learn.git
   zip -r anything-to-learn.zip anything-to-learn -x 'anything-to-learn/.git/*'
   ```
   不用命令行的话，也可以在 GitHub 页面点 **Code → Download ZIP**，解压后把文件夹从 `anything-to-learn-main` 改名为 `anything-to-learn`，再重新压缩。
2. 打开 **设置 → 功能（Settings → Capabilities）**，确认"代码执行与文件创建"已开启。
3. 在 **Skills** 区域点击 **上传 skill（Upload skill）**，选择 zip。
4. 在 Skills 列表里打开它的开关。

需要 Pro、Max、Team 或 Enterprise 计划（[官方说明](https://support.claude.com/en/articles/12512180-using-skills-in-claude)）。

</details>

<details>
<summary><b>Claude Code</b></summary>

```bash
git clone https://github.com/Looffeeuu/anything-to-learn.git ~/.claude/skills/anything-to-learn
```

只想在某个项目里用（例如课程作业仓库）：

```bash
git clone https://github.com/Looffeeuu/anything-to-learn.git .claude/skills/anything-to-learn
```

</details>

<details>
<summary><b>OpenAI Codex CLI</b></summary>

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/Looffeeuu/anything-to-learn.git ~/.agents/skills/anything-to-learn
```

</details>

<details>
<summary><b>Gemini CLI</b></summary>

```bash
gemini skills install https://github.com/Looffeeuu/anything-to-learn.git --scope user
gemini skills list    # 确认已安装
```

或者手动克隆到 `~/.gemini/skills/anything-to-learn`（也可以用 `~/.agents/skills/`）。

注：Google 已用 Antigravity CLI 替代部分账户类型的 Gemini CLI，使用前请以[官方文档](https://geminicli.com/docs/cli/skills/)为准。

</details>

<details>
<summary><b>Cursor</b></summary>

```bash
git clone https://github.com/Looffeeuu/anything-to-learn.git ~/.cursor/skills/anything-to-learn
```

Cursor 也会读取 `~/.agents/skills/` 和 `~/.claude/skills/`，用了通用安装就不必再装。

</details>

<details>
<summary><b>VS Code + GitHub Copilot</b></summary>

```bash
# 个人级
git clone https://github.com/Looffeeuu/anything-to-learn.git ~/.copilot/skills/anything-to-learn

# 或项目级（随仓库共享）
git clone https://github.com/Looffeeuu/anything-to-learn.git .github/skills/anything-to-learn
```

</details>

<details>
<summary><b>OpenCode</b></summary>

```bash
git clone https://github.com/Looffeeuu/anything-to-learn.git ~/.config/opencode/skills/anything-to-learn
```

OpenCode 也会读取 `~/.claude/skills/` 和 `~/.agents/skills/`。

</details>

<details>
<summary><b>其他支持 Agent Skills 的工具</b></summary>

把整个文件夹放到该工具读取 skill 的目录，文件夹名保持 `anything-to-learn`。如果它不自动发现，可以直接告诉它："读取 `<路径>/anything-to-learn/SKILL.md` 并按它的流程带我学习。"

</details>

### 不支持 skill 的聊天产品

ChatGPT、DeepSeek、Kimi、豆包等网页聊天产品没有 skill 文件夹，可以把 [`dist/anything-to-learn-single.md`](dist/anything-to-learn-single.md)（所有内容合并成的单文件版）粘贴进：

| 产品 | 放在哪 |
|---|---|
| ChatGPT | 新建 GPT 的 Instructions，或 Project 的指令 |
| 其他聊天产品 | 自定义指令 / 智能体设定 / 系统提示；没有的话，每次对话开头粘贴 |

这种方式能用，但有三点限制：

- **进度不会自动保存**。每次结束时它会给你一段进度摘要，下次开头粘贴回去即可接上。
- **"在你的代码里学"基本不可用**，因为它需要读文件、跑测试，只有 agent 类工具能做到。
- **材料识别取决于模型**。扫描版 PDF、板书照片、视频需要模型能看图、读文件。

### 验证与更新

安装后问它一句"你现在能用哪些 skill？"，列表里应该有 `anything-to-learn`。

更新到最新版：

```bash
git -C ~/.agents/skills/anything-to-learn pull    # 换成你的安装目录
```

用 skills CLI 安装的，重新运行一次 `npx skills add` 即可。Claude 网页版需要重新打包上传。

## 开始第一次学习

不需要特殊格式，正常说话就行：

```text
这是第 3 讲的 PPT 和板书照片，带我学一遍。
```

```text
下周三期中考，范围第 2–5 讲，这是前两年的卷子，帮我冲刺。
```

```text
我来给你讲一遍 attention，你挑毛病。
```

```text
继续上次的进度。
```

如果助手没有自动调用这个 skill，在开头加一句"用 anything-to-learn"。

学习过程中随时可以说：**"这个我会了"**（两三道快测，过了就跳）、**"直接告诉我"**（给答案）、**"我只有 15 分钟"**、**"慢一点"**、**"难一点"**、**"考试会考什么？"**。

## 工作原理

1. **摄取材料**：所有输入统一转成带出处的 `source-pack.md`，先给你看一屏目录，并标出没读清的地方，由你确认。
2. **学习地图**：整理出 4–10 项"学完能做什么"的能力，以及它们之间的依赖关系；有考试时，同时建立考试画像。
3. **学习**：每次开场 1–2 道热身题，然后按合适的教法讲新内容。程序性知识、概念、证明、论文、代码、记忆类内容，各有一套教法。
4. **练习**：有考试时用真题题型，学编程课时用你的代码，也可以换成你来讲。
5. **两行收尾**：今天学会了什么，下次从哪接着。没有作业。
6. **后台记账**：进度和误解地图静默更新，只用来决定下次的热身题和冲刺顺序。

所有状态都保存在你自己的学习文件夹里，是纯 Markdown，可以随时查看或迁移：

```
<course-name>/              （编程课放在作业仓库的 study/ 目录下）
├── source-pack.md     # 提取的材料，每段标注出处
├── learning-map.md    # 能力、依赖、关键因果链、常见误解
├── progress.md        # 学到哪、每个知识点的掌握状态
├── misconceptions.md  # 误解地图：错误信念、会影响什么、纠正进度
├── exam-profile.md    # 有考试时才有：题型、考点权重、常见套路
└── notes/             # 可选：你想留下的讲解或总结
```

## 学习科学依据

| 设计规则 | 依据 |
|---|---|
| 用检索练习代替重读 | [Rowland 2014](https://pubmed.ncbi.nlm.nih.gov/25150680/) · [Adesope et al. 2017](https://doi.org/10.3102/0034654316689306) |
| 间隔重现，薄弱项更早回来 | [Dunlosky et al. 2013](https://doi.org/10.1177/1529100612453266) · [Rawson & Dunlosky 2013](https://doi.org/10.1007/s10648-013-9240-4) |
| 新手先看例题，熟练后减少支架 | [van Gog, Paas & Sweller 2010](https://doi.org/10.1007/s10648-010-9145-4) · [Kalyuga 2007](https://doi.org/10.1007/s10648-007-9054-3) |
| 有基础时先尝试再讲解 | [Sinha & Kapur 2021](https://doi.org/10.3102/00346543211019105) |
| 反馈指出错误原因 | [Wisniewski, Zierer & Hattie 2020](https://doi.org/10.3389/fpsyg.2019.03087) · [Shute 2008](https://doi.org/10.3102/0034654307313795) |
| 交错练习训练方法选择 | [Brunmair & Richter 2019](https://pubmed.ncbi.nlm.nih.gov/31556629/) |
| 自我解释与反向讲授 | [Bisra et al. 2018](https://eric.ed.gov/?id=EJ1186664) |
| 警惕"看着都懂"的流畅性错觉 | [Koriat & Bjork 2005](https://doi.org/10.1037/0278-7393.31.2.187) |
| 学习者掌控节奏以维持动机 | [Ryan & Deci 2000](https://doi.org/10.1037/0003-066X.55.1.68) |

和原项目相比，这里有意用一部分强制性（必须自评把握、推送复习日程、不尝试就不给答案）换取更低的学习压力。我们的判断是：一个愿意持续回来的学习者，胜过一套完美但被放弃的制度。这个判断需要实测验证，见 [`evals/`](evals/scenarios.md)。

## 它不会做的事

- 不编造事实、公式、引用或往年真题；生成的练习题一律标注为生成
- 不替你写计分作业的提交答案，也不改你的作业文件让测试通过
- 不假装看过它没看过的视频、读过它没读的文件、跑过它没跑的代码
- 不承诺分数，考试预测只是估计
- 不推送复习提醒，不布置作业

## 项目结构

```
anything-to-learn/
├── SKILL.md                    # 主流程：agent 读取的入口
├── references/
│   ├── ingest.md               # 各类材料如何转成 source pack
│   ├── session.md              # 一次学习：热身、置信度推断、提示阶梯、状态感知
│   ├── lesson-modes.md         # 按材料类型选择教法
│   ├── progress.md             # 进度格式、热身题选择、冲刺模式
│   ├── exam-backsolve.md       # 应试反推：考试画像、得分计划、同构变式题、模考复盘
│   ├── misconceptions.md       # 误解地图：识别、确认、纠正、复查
│   ├── in-your-code.md         # 在学习者自己的代码和文件里学习
│   ├── teach-back.md           # 反向讲授
│   └── principles.md           # 学习科学依据（精简版）
├── evals/
│   └── scenarios.md            # 14 个模拟学习者测试场景
├── dist/
│   └── anything-to-learn-single.md   # 合并单文件版，供不支持 skill 的平台粘贴
├── README.md
└── LICENSE
```

## 状态与路线图

当前为 **v0.2 早期版本**，正在用 Stanford CS336 自学做第一轮实测。

- [x] 任意格式材料摄取与溯源
- [x] 隐式置信度推断、提示阶梯、热身题
- [x] 应试反推、误解地图、代码内学习、反向讲授
- [ ] 在 Claude Code、Codex CLI、Cursor 上跑通全部 eval 场景
- [ ] 补充一份真实学习记录作为示例
- [ ] 理科之外的课程（文科阅读、语言学习）实测

欢迎提 Issue 反馈使用体验。

## 致谢与许可

基于 [anything-to-course](https://github.com/lowwwbank/anything-to-course)（lowwwbank，MIT）改造：保留其学习科学内核，把"写一门课给别人上"改为"陪一个人自学"。

本项目采用 MIT 协议，并保留原项目的版权声明，见 [LICENSE](LICENSE)。
