import jieba
from collections import defaultdict


# ===============================
#  构建倒排索引（带词频和位置）
# ===============================
def build_inverted_index(documents):
    """
    documents: dict {doc_id: document_text}
    return: inverted_index
    """
    inverted_index = defaultdict(lambda: {
        "doc_ids": set(),
        "tf": defaultdict(int),
        "positions": defaultdict(list)
    })

    for doc_id, text in documents.items():

        # test = """
        #     全文检索技术是信息检索领域的重要研究方向。
        #     它通过构建倒排索引，实现大规模文档的快速搜索。
        #     相比顺序扫描，全文检索的效率更高。
        #     """,
        # 中文分词（专业做法），中文的分词工具jieba，hanl
        tokens = list(jieba.cut_for_search(text))

        for pos, token in enumerate(tokens):
            inverted_index[token]["doc_ids"].add(doc_id)
            inverted_index[token]["tf"][doc_id] += 1
            inverted_index[token]["positions"][doc_id].append(pos)

    return inverted_index


# ===============================
#  打印倒排索引
# ===============================
def print_inverted_index(index):
    for term, info in index.items():
        print(f"\n词: {term}")
        print(f"  出现在文档: {info['doc_ids']}")
        print(f"  词频(TF): {dict(info['tf'])}")
        print(f"  位置信息: {dict(info['positions'])}")


# ===============================
# 模拟文档数据
# ===============================
documents = {
    "doc1": """
    全文检索技术是信息检索领域的重要研究方向。
    它通过构建倒排索引，实现大规模文档的快速搜索。
    相比顺序扫描，全文检索的效率更高。
    """,

    "doc2": """
    现代搜索引擎普遍采用全文检索技术。
    倒排索引是全文检索系统的核心数据结构。
    百度、Google 都依赖倒排索引来实现毫秒级查询。
    """,

    "doc3": """
    中文分词是全文检索中非常关键的一步。
    分词质量直接影响搜索效果和召回率。
    常用工具包括 jieba、HanLP 等。
    """
}


# ===============================
#  主程序
# ===============================
if __name__ == "__main__":
    # index = build_inverted_index(documents)
    # print_inverted_index(index)
    t = jieba.cut_for_search("我爱北京天安门")
    # 0 我
    # 1 爱
    # 2 北京
    # 3 天安
    # 4 天安门
    t = jieba.cut("我爱北京天安门")
    print(t)
    # 0 我
    # 1 爱
    # 2 北京
    # 3 天安门

    for term, info in enumerate(t):
        print(term, info)

    t = jieba.lcut("我爱北京天安门")
    print(t)
    # cut        → 生成器，普通分词
    # lcut       → 列表，普通分词
    # cut_for_search → 生成器，搜索优化  分的词更小
    # lcut_for_search→ 列表，搜索优化