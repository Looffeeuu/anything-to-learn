# anything-to-learn

**给不想听课、想高效应试的理工科自学者的 AI 学习搭子：跑在你自己的文件里，从往年题倒推考点。**
把讲义、PPT、截图、板书照片、视频字幕、网页或者一个主题丢给它，它会整理成带出处的学习材料，然后按你的节奏一对一教你，下次回来时记得你学到哪、哪里薄弱。

*A low-pressure self-study tutor skill for people who skip the lecture on purpose. Any course material in, interactive learning out, progress carried across sessions.*

**和其他"把资料变成课"的工具不同，它的重点是：**
1. **应试反推**：上传往年题、作业、老师划的重点，分析题型和考点权重，按"每分钟换多少分"排学习顺序，生成同题型、同符号的变式题
2. **误解地图**：记录你"自信地错"背后的错误信念，先确认再纠正，并在它会影响的后续知识点之前先检查
3. **在你的代码里学**：读你的作业仓库，就你自己写的代码出题，先预测再运行，用测试判对错，报错时带你排查而不是直接改
4. **反向讲授**：你来讲，它扮演一个缺课但很聪明的同学，追问关键步骤、抛出常见误解
5. **可溯源**：每个知识点标注出自第几页 / 第几分钟，tutor 补充的内容单独标出

基于 [anything-to-course](https://github.com/lowwwbank/anything-to-course)（MIT）改造：保留它的学习科学内核，把"写一门课给别人上"改成"陪一个人自学"。

---

## 和普通 AI tutor / 原项目的区别

| | 课堂式 tutor | anything-to-learn |
|---|---|---|
| 置信度 | 每题手动标"确定/大概/猜" | tutor 从你的语气和推理里自己判断 |
| 复习 | 推送复习计划 | 没有计划；每次开场 1–2 道热身题，自动挑薄弱点 |
| 卡住时 | 不先尝试就不给答案 | 5 级提示阶梯，随时可以要答案，只记录不拒绝 |
| 教法 | 每课都先让你尝试 | 新手先看样例，有基础再先尝试 |
| 课程 | 一次性生成整门课 | 先出学习地图，课时按进度即时生成 |
| 考试 | 默认就有复习压力 | 你说"周五考试"才开启冲刺模式，按往年题反推重点 |
| 错题 | 记对错 | 记错误信念，以及它会连带影响哪些知识点 |
| 会了怎么办 | 照常走完 | 说"这个会了"→ 2–3 题快测，过了就跳 |

## 支持的输入

PDF（含扫描版）· PPT / 幻灯片 · Word / Markdown / 纯文本 · 截图、照片、板书 · 带字幕的视频文件 / 字幕文件 · 网页 · 代码仓库 / notebook · 往年试题 · 只给一个主题

在线视频链接无法直接观看，会请你提供字幕、讲稿或对应的 PPT。

## 用法

```text
用 anything-to-learn，这是第 3 讲的 PPT 和板书照片，带我学一遍。
```

```text
继续上次 CS336 的进度。
```

```text
下周三期中考，范围第 2–5 讲，这是前两年的卷子，帮我冲刺。
```

```text
我来给你讲一遍 attention，你挑毛病。
```

## 学习文件夹

```
<course-name>/
├── source-pack.md     # 从材料里提取的内容，每段标注出处（第几页 / 第几分钟）
├── learning-map.md    # 能力清单和依赖关系
├── progress.md        # tutor 的笔记本：学到哪、每个知识点的掌握状态
├── misconceptions.md  # 误解地图：错误信念、会影响什么、纠正进度
├── exam-profile.md    # 有考试时才有：题型、考点权重、常见套路
└── notes/             # 可选：你想留下的讲解或总结
```

`progress.md` 是 tutor 自己用的，不是给你的待办事项。

## 项目结构

```
SKILL.md                    # 主流程
references/
  ingest.md                 # 各类材料怎么转成 source pack
  session.md                # 一次学习怎么进行：热身、置信度推断、提示阶梯、状态感知
  lesson-modes.md           # 按材料类型选择教法（程序性 / 概念 / 证明 / 论文 / 代码 / 记忆）
  progress.md               # 进度格式、热身题选择、冲刺模式
  exam-backsolve.md         # 应试反推：考试画像、每分钟得分计划、同构变式题、模考复盘
  misconceptions.md         # 误解地图：识别、确认、纠正、复查
  in-your-code.md           # 在学习者自己的代码和文件里学习
  teach-back.md             # 反向讲授
  principles.md             # 学习科学依据（精简版）
evals/
  scenarios.md              # 模拟学习者测试场景
```

## 安装

把整个文件夹放进你的 agent 的 skills 目录（例如 Claude Code 的 `~/.claude/skills/anything-to-learn/`），或在 Claude.ai 里作为 skill 上传。

## 状态

v0.2，早期草稿，正在用 Stanford CS336 自学做第一轮实测。

## License

MIT。保留原项目 anything-to-course 的版权声明。
