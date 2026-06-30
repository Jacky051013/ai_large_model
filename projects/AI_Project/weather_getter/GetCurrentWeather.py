import os
import requests
from dotenv import load_dotenv
from langchain.agents import create_agent,AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
weather_api_key = os.getenv("OPENWEATHER_API_KEY")

@tool
def get_current_weather(city):
    """
    查询指定城市的当前天气。
    参数: city - 城市名（英文或拼音，如 Beijing, Shanghai）
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": weather_api_key,
        "units": "metric",
        "lang": "zh_cn"
    }
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        if response.status_code == 200:
            weather_desc = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            return (
                f"城市：{city}\n"
                f"天气：{weather_desc}\n"
                f"温度：{temp}°C\n"
                f"体感温度：{feels_like}°C\n"
                f"湿度：{humidity}%"
            )
        else:
            return f"查询失败：{data.get('message', '未知错误')}"
    except Exception as e:
        return f"请求异常：{str(e)}"

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=openai_api_key)
tools = [get_current_weather]

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个天气查询助手，会根据用户问题调用工具获取真实天气，然后用自然语言回答。"),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_agent(llm=model, tools=tools, prompt=prompt)
agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True)

if __name__ == "__main__":
    query = "今天北京天气怎么样？"
    result = agent_executor.invoke({"input": query})
    print("\n===== 最终回答 =====")
    print(result["output"])


