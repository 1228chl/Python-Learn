from langchain_openai import ChatOpenAI
from typing import Optional
from pydantic import BaseModel, Field  # 数据模型，数据结构。做数据类型类型校验，尤其是API接口
from langchain.agents import create_agent
import os

# 第一步：定义你想要的输出结构（Pydantic 模型）
class PersonInfo(BaseModel):
    name: str = Field(description="人的姓名")
    age: int = Field(description="人的年龄,单位:岁")
    city: Optional[str] = Field(default=None,description="居住城市")

# 第二步：初始化 LLM
llm = ChatOpenAI(
    model="qwen-max",
    api_key=os.getenv("TONGYI_API_KEY"),
    base_url=os.getenv("TONGYI_BASE_URL"),
    temperature=0)

# 第三步：绑定结构化输出格式
agent = create_agent(
    model=llm,
    response_format=PersonInfo,# 绑定结构化输出格式
)

# 第四步：调用
user_input = "我叫李明，我喜欢打篮球，看NBA，我今年28岁，先谢谢谢谢，之前住在深圳，现在住在上海。"
response = agent.invoke(
    {"messages": [{"role": "user", "content": user_input}]}
)

# 输出结果
print(response)
result = response['structured_response']

# 可以直接访问字段
print(f"姓名: {result.name}, 年龄: {result.age}, 城市: {result.city}")