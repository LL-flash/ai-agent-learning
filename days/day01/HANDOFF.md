# Day1-HANDOFF.md

# AI Agent 实习冲刺计划 - Day 1

## 日期

Day 1

## 今日目标

建立对大语言模型（LLM）应用开发的第一层认知，理解 LLM API 的基本工作方式，并独立完成第一个基于 API 的 Terminal Chat Assistant。

今天的重点不是学习复杂框架，而是建立：

> 用户输入 → 消息组织 → 模型调用 → 模型响应 → 上下文管理

这一条完整链路的理解。

---

# 一、今日核心目标

完成以下能力：

* 能够调用大语言模型 API
* 理解 Chat Completion 的基本结构
* 理解 messages 机制
* 理解 System Prompt 的作用
* 理解多轮对话如何实现
* 完成第一个 CLI 聊天机器人
* 建立 GitHub 项目记录习惯

---

# 二、项目初始化

## 创建项目

项目名称：

```
agent-learning
```

目录结构：

```
agent-learning/

├── README.md

├── .gitignore

├── requirements.txt

├── app.py

├── notes/

│   └── day1.md

└── projects/
```

---

# 三、环境准备

确认安装：

* Python 3.11+
* VS Code
* Git
* GitHub账号

推荐：

使用虚拟环境管理依赖。

---

# 四、今日学习内容

## 1. Chat Completion API

核心理解：

一次模型调用包含：

```
用户输入

↓

messages

↓

模型

↓

response

↓

输出结果
```

重点理解四个对象：

---

## client

作用：

负责连接模型服务。

例如：

```
客户端程序
    |
    |
    ↓
LLM API
```

---

## messages

作用：

保存当前对话上下文。

结构：

```
[
    system message,
    user message,
    assistant message
]
```

理解：

模型本身不会记住聊天历史。

每一次请求，都需要客户端重新提供上下文。

---

## model

作用：

指定使用哪个模型。

例如：

不同模型：

* 能力不同
* 速度不同
* 成本不同

---

## response

作用：

保存模型返回结果。

需要观察完整返回结构：

包括：

* 回复内容
* token 使用量
* 请求信息
* 时间信息

---

# 五、代码实验任务

## 实验1：基础调用

完成：

输入一句话。

模型返回回答。

目标：

理解一次完整请求流程。

---

## 实验2：System Prompt实验

测试不同角色：

例如：

```
你是一名Python老师
```

```
你是一名海盗
```

```
你是一名严格的数学教授
```

观察：

同一个问题为什么会产生不同回答。

---

## 实验3：多轮聊天

实现：

```
User

↓

Assistant

↓

User

↓

Assistant
```

核心：

不断维护：

```
messages.append()
```

---

## 实验4：查看Response结构

不要直接获取答案。

先打印完整response。

观察：

* choices
* usage
* id
* created

理解每个字段作用。

---

# 六、必须完成的思考题

完成后写入：

```
notes/day1.md
```

回答：

---

## 1. 为什么 messages 是 list？

要求：

解释为什么聊天记录需要按照顺序保存。

---

## 2. 为什么需要 system message？

要求：

解释：

System Prompt 为什么可以影响模型行为。

---

## 3. 为什么 assistant 的回答也需要保存？

要求：

解释：

为什么下一轮对话需要知道模型之前说过什么。

---

## 4. 为什么聊天越久成本越高？

要求：

解释：

Token 增长和上下文长度的关系。

---

# 七、Git提交要求

第一次提交：

Commit message：

```
feat: build first terminal chatbot
```

提交内容：

* 项目结构
* API调用代码
* 多轮聊天代码
* 学习笔记

---

# 八、今日输出成果

完成 Day1 后，应拥有：

## 代码成果

```
app.py

可以运行：

python app.py
```

实现：

* 输入问题
* 获取回答
* 连续聊天

---

## 文档成果

```
notes/day1.md
```

记录：

* 今天学到什么
* 遇到什么问题
* 如何解决
* 还有哪些疑问

---

## GitHub成果

仓库：

```
agent-learning
```

包含第一次提交。

---

# 九、今日禁止事项

今天不要学习：

* LangChain
* LangGraph
* CrewAI
* RAG
* MCP
* Fine-tuning
* Transformer源码

原因：

当前目标是理解 LLM 应用最基本工作流程。

先建立底层认知，再学习框架。

---

# 十、Day1完成标准

达到以下标准：

能够回答：

---

## Q1：ChatGPT为什么能够连续聊天？

答案方向：

因为客户端保存并传递历史 messages，而不是模型永久保存聊天记录。

---

## Q2：System Prompt为什么有效？

答案方向：

因为它属于输入上下文的一部分，会影响模型生成结果。

---

## Q3：为什么Token影响成本？

答案方向：

因为模型处理的是Token数量，上下文越长，每次请求输入越多。

---

# Day1结束检查清单

* [ ] 环境配置完成
* [ ] 创建agent-learning项目
* [ ] 完成API调用
* [ ] 完成Prompt实验
* [ ] 完成多轮聊天
* [ ] 查看response结构
* [ ] 完成Git提交
* [ ] 写学习总结

---

# Day1核心思想

不要追求学很多。

今天的目标：

> 搞懂一个LLM应用最小闭环。

从今天开始，所有学习围绕：

理解 → 实验 → 输出 → 复盘

进行。
