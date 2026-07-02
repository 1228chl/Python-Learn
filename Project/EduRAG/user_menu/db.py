'''
离线知识库搭建
1.读取PDF文件，List[Document]
2.文档切块

创建文档分割器，执行切分chunk
3.向量化与存储
对于上面的chunk编码，存储到向量数据库[chroma]
4.返回检索器
'''
import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from models import embedding
from langchain_community.vectorstores import Chroma

def create_db(file_path,embedding,persist_directory="./chroma.db"):
    '''
    读取file_path的pdf文件，创建向量是数据库，返回检索器
    '''
    if os.path.exists(persist_directory):
        vector_store = Chroma(persist_directory)
        return vector_store.as_retriever()

    # 1.读取PDF文件，List[Document]
    loader = PyMuPDFLoader(file_path)
    docs = loader.load()
    print(docs)

    # 2.文档切块
    # 创建文档分割器，执行切分chunk
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=10,
    )
    chunks = text_splitter.split_documents(docs)
    print(chunks)
    # 3.向量化与存储
    # 对于上面的chunk编码，存储到向量数据库[chroma]
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=persist_directory
    )
    # 4.返回检索器
    retriever = vector_store.as_retriever(search_kwargs={"k": 2})
    return retriever


if __name__ == '__main__':
    retriever = create_db("./data/物流信息.pdf" ,embedding)
    print(retriever.invoke("我用的哪个快递公司"))