from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(
    model="qwen-max",
    api_key=os.getenv("TONGYI_API_KEY"),
    base_url=os.getenv("TONGYI_BASE_URL"),
    extra_body={"enable_thinking": False}
)

agent = create_agent(
    model=llm,
    checkpointer=InMemorySaver(),
)

print("agent对象：",agent)
config = {"configurable":{"thread_id":"1"}}

print(agent.invoke(
    {"messages":[{"role":"user","content":"你能做什么"}]},
    config = config,
))
print(agent.invoke(
    {"messages":[{"role":"user","content":"小明有3个苹果和4个李子，他一共有几个水果"}]},
    config,
))
result = agent.invoke(
    {"messages": [{"role": "user", "content": "我问了几个问题了"}]},
    {"configurable": {"thread_id": "2"}},
)
print(result["messages"][-1].content)