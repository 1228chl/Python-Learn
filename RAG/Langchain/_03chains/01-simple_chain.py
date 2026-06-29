from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(
    model="qwen-max",
    api_key=os.getenv("TONGYI_API_KEY"),
    base_url=os.getenv("TONGYI_BASE_URL"),
    extra_body={"enable_thinking": False}
)

prompt = PromptTemplate(
    template="我的邻居姓{lastname}，他生了个儿子，给他儿子起一个名字，起3个最好听的名字",
    input_variables=["lastname"],
)

chain = prompt | llm
print(chain.invoke({"lastname": "赵"}).content)
