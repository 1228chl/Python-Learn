from langchain_core.prompts import PromptTemplate
import os

from langchain_openai import ChatOpenAI

# 定义模板
# template = "我的邻居姓{lastname}，他生了个儿子，给他儿子起个名字"
#
# prompt = PromptTemplate(
#     # input_variables=["lastname"],
#     template=template,
# )
prompt = PromptTemplate.from_template("我的邻居姓{lastname}，他生了个儿子，给他儿子起个名字")

prompt_text = prompt.format(lastname="包")
print(prompt_text)
# result: 我的邻居姓王，他生了个儿子，给他儿子起个名字

llm = ChatOpenAI(
    model="qwen-max",
    api_key = os.getenv("TONGYI_API_KEY"),
    base_url = os.getenv("TONGYI_BASE_URL"),
)

result = llm.invoke(prompt_text)
print(result.content)