import os
from langchain_community.embeddings import DashScopeEmbeddings # 百炼平台

embedding_model = DashScopeEmbeddings(
    dashscope_api_key=os.getenv('TONGYI_API_KEY'),
    model='test-embedding-v4'
)
print(embedding_model.embed_query('你好..'))
print(embedding_model.embed_documents(['你好..','ajadjasdkklasd']))




