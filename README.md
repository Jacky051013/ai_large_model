# AI Large Model Course

这个仓库整理自本地课程目录：

`/Users/jacky/jupyter_notebook/AI大模型课程`

内容以 Jupyter Notebook 为主，覆盖大模型 API 调用、提示工程、LangChain 基础组件、记忆、RAG 和 Agent 等主题。

## 目录结构

```text
.
├── basic_API/            # 大模型 API 请求、token 计数、常用参数
├── AI_prompt/            # 提示工程：输出格式、零样本/小样本、思维链
├── input_output_of_AI/   # LangChain 模型、Prompt Template、Output Parser、Chain
├── memory/               # 对话记忆与不同 Memory 类型
├── RAG/                  # 文档加载、文本切分、Embedding、Vector Store、Retrieval Chain
├── Agent/                # Agent、Tools、代码执行和表格分析示例
├── use_of_AI_api/        # 文本总结、撰写、分类、翻译 API 示例
└── *.ipynb               # 课程演示和综合练习 Notebook
```

## 课程内容

- 大模型 API 基础：发送请求、理解 token 计费、调整生成参数。
- 提示工程：限定输出格式、零样本与小样本提示、分步骤思考。
- LangChain 基础：模型封装、提示模板、输出解析器和链式调用。
- Memory：让对话链保留上下文，比较不同记忆类型。
- RAG：加载外部文档、文本切分、向量嵌入、向量存储和检索增强生成。
- Agent：自定义工具、执行 Python 代码、使用工具分析数据表格。
- API 应用案例：文本总结、文案撰写、问题分类和文本翻译。

## 运行方式

建议使用 Python 3.10 或更高版本。

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

使用大模型 API 的 Notebook 需要先在本地设置环境变量：

```bash
export OPENAI_API_KEY="你的 API Key"
```

部分 Notebook 使用了自定义 `OPENAI_BASE_URL` 或兼容 OpenAI API 的第三方接口，请根据自己的服务地址调整。

## 安全说明

- 上传前已移除真实 API key，Notebook 中只保留环境变量或占位符示例。
- 不要把自己的 API key、访问令牌、密码等敏感信息直接写入 Notebook 后提交到 GitHub。
- 仓库已忽略 `.DS_Store`、`.ipynb_checkpoints/`、虚拟环境和 Python 缓存文件。
