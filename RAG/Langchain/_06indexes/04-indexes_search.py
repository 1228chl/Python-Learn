from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import DashScopeEmbeddings
import os

loader = TextLoader('../data/pku.txt')
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = DashScopeEmbeddings(
    model="test-embedding-v1",  # test-embedding-v3
    dashscope_api_key=os.getenv('TONGYI_API_KEY')
)

db = Chroma.from_documents(texts,embeddings,persist_directory="outputs/Chroma.db")
retriever = db.as_retriever(search_kwargs={"k": 1})
docs = retriever.invoke("北京大学什么时候成立的")
print(docs)