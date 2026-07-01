from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
import os

# pku.txt内容：<https://www.pku.edu.cn/about.html>
# 1. 读取文档
with open('../data/pku.txt',encoding='utf-8') as f:
    state_of_the_union = f.read()
# 文档分割
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=20)

texts = text_splitter.split_text(state_of_the_union)
print(texts)

# 3. 向量化，创建embedding模型
embeddings = DashScopeEmbeddings(
    model="test-embedding-v1",  # test-embedding-v3
    dashscope_api_key=os.getenv('TONGYI_API_KEY')
)

# 4. 创建向量数据库
docsearch = Chroma.from_texts(texts, embeddings, persist_directory="outputs/chroma.db")

# 5. 测试检索
query = "1937年北京大学发生了什么？"
docs = docsearch.similarity_search(query, k=2)
print("长度为", len(docs), docs)

'''
[Document(page_content='1937年卢沟桥事变后，北京大学与清华大学、南开大学南迁长沙，共同组成国立长沙临时大学。1938年，临时大学又西迁昆明，更名为国立西南联合大学。抗日战争胜利后，北京大学于1946年10月在北平复员。'), Document(page_content='北京大学创办于1898年，是戊戌变法的产物，也是中华民族救亡图存、兴学图强的结果，初名京师大学堂，是中国近现代第一所国立综合性大学，辛亥革命后，于1912年改为现名。'), Document(page_content='在悠久的文明历程中，古代中国曾创立太学、国子学、国子监等国家最高学府，在中国和世界教育史上具有重要影响。北京大学“上承太学正统，下立大学祖庭”，既是中华文脉和教育传统的传承者，也标志着中国现代高等教育的开端。其创办之初也是国家最高教育行政机关，对建立中国现代学制作出重要历史贡献。'), Document(page_content='1917年，著名教育家蔡元培就任北京大学校长，他“循思想自由原则，取兼容并包主义”，对北京大学进行了卓有成效的改革，促进了思想解放和学术繁荣。陈独秀、李大钊、毛泽东以及鲁迅、胡适、李四光等一批杰出人士都曾在北京大学任教或任职。')]
'''
# 创建检索器
retriever = docsearch.as_retriever(search_kwargs={"k": 2})
print("长度为", len(docs), retriever.invoke(query))