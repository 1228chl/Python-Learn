from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

# llm = ChatOpenAI(
#     api_key=os.getenv("API_KEY"),
#     model="qwen3.5-flash",
#     base_url=os.getenv("BASE_URL"),
#     extra_body={"enable_thinking": False}
# )

llm = init_chat_model(
    model="qwen-max",
    api_key=os.getenv("TONGYI_API_KEY"),
    base_url=os.getenv("TONGYI_BASE_URL"),
    model_provider="openai",
)

# 创建第一条链
first_prompt = PromptTemplate.from_template("我的邻居姓{lastname}，他生了个儿子，给他儿子起个名字")

# 创建第二条链
second_prompt = PromptTemplate.from_template(
    "邻居的儿子名字叫{child_name}，给他起一个小名",
)

# 链接两条链
chain = first_prompt | llm | second_prompt | llm | StrOutputParser()

# 执行链，只需要传入第一个参数
output = chain.invoke({"lastname": "孙"})
print(output)
# print(output.content)