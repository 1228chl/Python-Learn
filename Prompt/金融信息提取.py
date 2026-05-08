import json
from openai import OpenAI

# 1.提供一些例子供模型参考
ie_examples = [
    {
        'content': '2023-01-10，股市震荡。股票古哥-D[EOOE]美股今日开盘价100美元，一度飙升至105美元，随后回落至98美元，最终以102美元收盘，成交量达到520000。',
        'answers': {
            '日期': ['2023-01-10'],
            '股票名称': ['古哥-D[EOOE]美股'],
            '开盘价': ['100美元'],
            '收盘价': ['102美元'],
            '成交量': ['520000'],
        }
    }
]

# 2 构建函数，进行prompt设计（描述清楚任务及输出格式）
IE_PATTERN = "{}\n\n提取上述句子中的实体，并输出，上述句子中不存在的信息用['原文中未提及']来表示。"


def build_prompt(ie_examples):
    history_list = [{'role': 'system',
                     'content': "你是信息提取专家，需要需要完成信息抽取任务。"
                                "我会给你一个句子，你需要提取句子中的实体，并输出，如果句子中有不存在的信息用['原文中未提及']来表示。"}]

    # 遍历示例，将样本和实体 添加到history_list中
    for example in ie_examples:  # 遍历每个样本
        sentence = example['content']
        # 获取到金融类型需要抽取的实体
        history_list.append({'role': 'user', 'content': IE_PATTERN.format(sentence)})
        history_list.append({'role': 'assistant', 'content': json.dumps(example['answers'],ensure_ascii=False)})

    return {'history_list': history_list}


# 3 构建推理函数
def model_chat(content: str, history=[]) -> str:
    """
    调用大模型对话接口
    :param messages: 输入内容
    :param model: 模型名称
    :return: 大模型输出内容 str
    """
    client = OpenAI(
        api_key='sk-49248a9a9fe8448f89007c71a3a21600',
        base_url="https://api.deepseek.com")
    messages = [{'role': 'user', 'content': content}]
    response = client.chat.completions.create(
        model='deepseek-chat',
        messages=messages+history,
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}})
    return response.choices[0].message.content


# 4 调用推理
sentences = [
    '2025-02-15，寓意吉祥的节日，股票佰笃[BD]美股开盘价10美元，虽然经历了波动，但最终以13美元收盘，成交量微幅增加至460,000，投资者情绪较为平稳。',
    '2025-04-05，市场迎来轻松氛围，股票盘古(0021)开盘价23美元，尽管经历了波动，但最终以26美元收盘，成交量缩小至310,000，投资者保持观望态度。',
]

prompt_dict = build_prompt(ie_examples)
for sentence in sentences:
    print(f'sentence-->{sentence}')
    result = model_chat(sentence, prompt_dict['history_list'])
    print(result)