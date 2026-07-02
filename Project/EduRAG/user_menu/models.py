'''
1.embedding模型 dashscope
2.对话大模型
'''
import os
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_openai import ChatOpenAI

embedding = DashScopeEmbeddings(
    dashscope_api_key=os.getenv('TONGYI_API_KEY'),
    model="text-embedding-v3"
)

llm = ChatOpenAI(
    base_url = os.getenv("TONGYI_BASE_URL"),
    api_key = os.getenv("TONGYI_API_KEY"),
    model="qwen-max",
)

if __name__ == '__main__':
    print(embedding.embed_query("ai 好啊，得学啊"))
    print(llm.invoke("你好") )