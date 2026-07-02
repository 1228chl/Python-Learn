'''
1.query向量化
2.用retriever检索处topk上下文
3.写完整的提示词，包含query和topk(str)内容
4.调用大模型生成完整的回答
'''
from db import create_db
from models import embedding,llm
from langchain_core.prompts import PromptTemplate

retriever = create_db(
    file_path=r'./data/物流信息.pdf',
    embedding=embedding,
    persist_directory="./chroma.db"
)

def main():
    query = "我的快递从哪发货"
    # 用retriever检索处topk上下文
    top_k = retriever.invoke(query) # List[Document]
    print(f'检索出的上下文有{len(top_k)}个',top_k)
    context = "\n\n".join([doc.page_content for doc in top_k]) # List[Document] -> 拼接成str字符串
    # 写完整的提示词，包含query和topk(str)内容
    prompt = PromptTemplate.from_template(f"""
    请根据检索的内容回答用户的问题。
    如果检索的内容不足以回答用户的问题，请回答“检索信息不足，无法回答”，不要添加任何多余的内容。
    你不能基于自己的知识回答，或者回答与用户问题无关的信息。
    问题：{query}
    检索内容：{context}
    请回答用户的问题
    """)
    # 调用大模型生成完整的回答
    answer = llm.invoke(prompt.format_prompt(query=query,context=context))
    print(answer.content)

if __name__ == '__main__':
    main()