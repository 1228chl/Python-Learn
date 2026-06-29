import os
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_community.tools import DuckDuckGoSearchRun

# 初始化工具
ddg_search = DuckDuckGoSearchRun()

# 实例化大模型
llm = ChatOpenAI(
    api_key=os.getenv('TONGYI_API_KEY'),
    model="qwen-max",
    base_url=os.getenv("TONGYI_BASE_URL"),
    extra_body={"enable_thinking": False}
)

agent = create_agent(
    model=llm,
    tools=[ddg_search],
    system_prompt="""你是一个有用的个人助手，根据用户的输入内容选择对应的工具，解答用户的问题"""
)

print('agent',agent)

# 代理Agent工作
response = agent.invoke(
    {
        "messages":[
            {
                "role":"user",
                "content":"中国目前有多少人口，给具体时间和数量"
            }
        ]
    }
)
for msg in response['messages']:
    print(msg.content)