# anything-to-learn

**给不想听课、想更高效自学的人的低压力学习 tutor skill。**
把讲义、PPT、截图、板书照片、视频字幕、网页或者一个主题丢给它，它会整理成带出处的学习材料，然后按你的节奏一对一教你，下次回来时记得你学到哪、哪里薄弱。

*A low-pressure self-study tutor skill for people who skip the lecture on purpose. Any course material in, interactive learning out, progress carried across sessions.*

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
| 考试 | 默认就有复习压力 | 你说"周五考试"才开启冲刺模式 |
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
下周三期中考，范围第 2–5 讲，帮我冲刺。
```

## 学习文件夹

```
<course-name>/
├── source-pack.md     # 从材料里提取的内容，每段标注出处（第几页 / 第几分钟）
├── learning-map.md    # 能力清单和依赖关系
├── progress.md        # tutor 的笔记本：学到哪、每个知识点的掌握状态
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
  principles.md             # 学习科学依据（精简版）
evals/
  scenarios.md              # 模拟学习者测试场景
```

## 安装

把整个文件夹放进你的 agent 的 skills 目录（例如 Claude Code 的 `~/.claude/skills/anything-to-learn/`），或在 Claude.ai 里作为 skill 上传。

## 状态

v0.1，早期草稿，正在用 Stanford CS336 自学做第一轮实测。

## License

MIT。保留原项目 anything-to-course 的版权声明。
