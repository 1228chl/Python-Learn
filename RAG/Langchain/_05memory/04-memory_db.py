from langchain.agents import create_agent
from langgraph.checkpoint.mysql.pymysql import PyMySQLSaver
from langchain_openai import ChatOpenAI
import os
import uuid  # 模拟创建用户id

llm = ChatOpenAI(
    model="qwen-max",
    api_key=os.getenv("TONGYI_API_KEY"),
    base_url=os.getenv("TONGYI_BASE_URL"),
    extra_body={"enable_thinking": False}
)

# 注意：这里使用的是 pymysql 驱动
# http://baidu.com
DB_URL = f"mysql+pymysql://root:123456@localhost:3306/langchain_db?charset=utf8mb4"

# 使用上下文管理器初始化 MySQL 连接
# MySQLSaver 通常会自动处理表的创建，或者你可以显式调用 setup 方法（取决于具体版本）
with PyMySQLSaver.from_conn_string(DB_URL) as checkpointer:
    # 确保数据库表已创建（视版本而定，部分版本自动创建）
    checkpointer.setup()

    agent = create_agent(
        llm,
        tools=[],
        checkpointer=checkpointer,# 传入MySQL检查点实例
    )

    # 在这里调用agent进行测试
    # agent.invoke(...)
    print(agent)
    config = {"configurable":{"thread_id":uuid.uuid4()}}
    print(agent.invoke(
        {"messages":[{"role":"user","content":"你能做什么"}]},
        config=config
    ))
    print(agent.invoke(
        {"messages": [{"role": "user", "content": "小明有3个苹果和4个李子，他一共有几个水果"}]},
        config,
    ))
    result = agent.invoke(
        {"messages": [{"role": "user", "content": "我问了几个问题了"}]},
        config,
    )
    print(result['messages'][-1].content)