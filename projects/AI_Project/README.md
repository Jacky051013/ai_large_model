# AI Project Collection

这是一个 AI 应用项目集合，包含多个基于大模型、LangChain、Streamlit、RAG 和工具调用的练习项目。每个子目录都是一个相对独立的小应用或实验。

## 项目列表

- `cloned_chatgpt/`：基于 Streamlit 和 LangChain Memory 的简易聊天机器人。
- `Video_script_generator/`：根据主题、时长和创意程度生成视频脚本。
- `xiaohongshu_generator/`：生成小红书风格标题和正文内容。
- `csv-analyzer/`：上传 CSV 后用大模型辅助分析表格数据。
- `pdf-qa-tool/`：PDF 问答工具，包含向量检索、重排和对话式问答示例。
- `RAG_demo/`：RAG 与 OpenAI API 调用的基础演示。
- `weather_getter/`：结合天气 API 和大模型的工具调用示例。

## 运行方式

进入具体项目目录后，按该项目的依赖文件安装环境。例如：

```bash
cd projects/AI_Project/cloned_chatgpt
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run main.py
```

如果项目使用 `requirement.txt`，则对应执行：

```bash
pip install -r requirement.txt
```

## 环境变量

涉及大模型 API 或外部服务的项目需要在本机配置环境变量：

```bash
export OPENAI_API_KEY="你的 API Key"
export OPENWEATHER_API_KEY="你的 OpenWeather API Key"
```

不要把 API key、token、Cookie 等敏感信息写入代码或提交到 GitHub。

## 说明

- `.venv/`、`.idea/`、`__pycache__/` 等本地环境和缓存目录不会提交。
- 项目里的 PDF、CSV 等文件是示例数据，用于演示 RAG、表格分析和问答流程。
- 各项目依赖可能不同，建议分别创建虚拟环境运行。
