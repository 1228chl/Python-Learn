from langchain.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(
    model="qwen-max",
    api_key=os.getenv("TONGYI_API_KEY"),
    base_url=os.getenv("TONGYI_BASE_URL"),
    extra_body={"enable_thinking": False}
)
messages = [
    HumanMessage(content="你好"),
    AIMessage(content="你好，有什么可以帮你？"),
    HumanMessage(content="LangChain 是什么？"),
    AIMessage(content="LangChain 是一个开源的 LLM 应用开发框架，用于构建 LLM 应用。"),
    HumanMessage(content="我问了几个问题了？"),
]

response = llm.invoke(messages)
print(response.content)
# messages = []
# while True:
#     messages.append(
#         HumanMessage(content=input("[请输入问题]"))
#     )
#     response = llm.invoke(messages)
#     print("[大模型回答]\n", response.content)
#     messages.append(AIMessage(content=response.content))
#
#     if len(messages) > 5:
#         messages = messages[-5:]
#
#     print("\n当前历史对话：")
#     for msg in messages:
#         print(f"{msg.content}")