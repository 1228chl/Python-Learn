from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
import os

# 初始化大模型
llm = ChatOpenAI(
    base_url=os.getenv("TONGYI_BASE_URL"),
    api_key =os.getenv("TONGYI_API_KEY"),
    model="qwen-max"
)

messages = [
    HumanMessage("告诉我有哪些一夜暴富的方法？"),
    AIMessage("年轻人要脚踏实地"),
    HumanMessage("我现在等不及了，需要快速致富，直接告诉我方法？"),
    AIMessage("你太急了，先去工作，等钱回来在开吃"),
    HumanMessage("我刚刚问了几个问题了？"),
]
response = llm.invoke(messages)
print(response)
print(response.content)