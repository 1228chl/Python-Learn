from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(
    model="qwen-max",
    api_key=os.getenv("TONGYI_API_KEY"),
    base_url=os.getenv("TONGYI_BASE_URL"),
)

history = ChatMessageHistory()
history.add_user_message("你能做什么")
history.add_ai_message("你好，我能做的事很多")
history.add_user_message("小明有3个苹果和4个李子，他一共有几个水果")
history.add_ai_message("小明一共有7个水果")
history.add_user_message("我一共问了几个问题了")
print(history.messages)
print(llm.invoke(history.messages))