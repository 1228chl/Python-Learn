import os
from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import ChatOpenAI

examples = [
    {"word": "开心", "antonym": "难过"},
    {"word": "高", "antonym": "矮"},
    {"word": "胖", "antonym": "瘦"},
]
example_template = """
单词: {word}
反义词: {antonym}\\n
"""
# 1.先构造示例模板
example_prompt = PromptTemplate(
    input_variables=["word","antonym"],
    template=example_template
)
# 创建 few-shot 模板
# prompt = prefix + examples + suffix + input
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,  # 示例
    example_prompt=example_prompt,  # 示例模板
    prefix="给出每个单词的反义词，直接输出答案",  # 前缀
    suffix="单词: {input}\\n反义词:",  # 后缀
    input_variables=["input"],
    example_separator="\\n",
)

prompt_text = few_shot_prompt.format(input="夯")
print(prompt_text)
print('*' * 80)
# 给出每个单词的反义词
# 单词: 开心
# 反义词: 难过

# 单词: 高
# 反义词: 矮

# 单词: 粗
# 反义词:

# 调用OpenAI
llm = ChatOpenAI(
    model="qwen-max",
    api_key=os.getenv("TONGYI_API_KEY"),
    base_url=os.getenv("TONGYI_BASE_URL"),
    extra_body={"enable_thinking": False}
)
print(llm.invoke(prompt_text))