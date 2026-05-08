from openai import OpenAI
# import dashscope
# dashscope.api_key = 'sk-e9d40ca8abe14210b194202a5505216b'
# response = dashscope.Generation.call(
#     model='qwen3.5-35b-a3b',
#     messages=[
#     {'role': 'system', 'content': '你好，我需要你的帮助'},
#     {'role': 'user', 'content': '你是谁？'}
# ])
# print(response.message)


# client = OpenAI(
#     api_key="sk-c0omjpjfngnozpio4tf1nkmlywlnihzochr97lm7rvbyun3e",
#     base_url="https://api.xiaomimimo.com/v1"
# )
#
# completion = client.chat.completions.create(
#     model="mimo-v2.5-pro",
#     messages=[
#         {
#             "role": "system",
#             "content": "You are MiMo, an AI assistant developed by Xiaomi. Today is date: Tuesday, December 16, 2025. Your knowledge cutoff date is December 2024."
#         },
#         {
#             "role": "user",
#             "content": "你好啊，给我讲个笑话吧？"
#         }
#     ],
#     max_completion_tokens=1024,
#     temperature=1.0,
#     top_p=0.95,
#     stream=False,
#     stop=None,
#     frequency_penalty=0,
#     presence_penalty=0
# )
#
# print(completion.model_dump_json())

# client = OpenAI(
#     api_key='sk-49248a9a9fe8448f89007c71a3a21600',
#     base_url="https://api.deepseek.com")
#
# sp = """你是一个快递信息提取专家，能够根据用户输入的快递地址、人名、手机号信息把对应的实体抽取出来，并以JSON格式返回。比如输入：张明远，138-1234-5678
# 广东省深圳市南山区科技园南区高新南一道1000号腾讯大厦18层 1806室，你返回：
# {
#   "name": "张明远",
#   "phone": "138-1234-5678",
#   "address": "广东省深圳市南山区科技园南区高新南一道1000号腾讯大厦18层 1806室"
# }
#
# 需要注意，对于用户的输入，你只返回上述的json格式，不要返回任何其他内容。
# """
#
# up = """
# 李婉婷
# 151-9876-5432
# 北京市海淀区中关村大街1号海龙大厦8层805室
# 东西是一份文件，已经封装好了。寄普通快递就行，麻烦寄出后把单号发我一下，谢谢啦！
# """
#
# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": sp},
#         {"role": "user", "content": up},
#     ],
#     stream=False,
#     reasoning_effort="high",
#     extra_body={"thinking": {"type": "enabled"}}
# )
#
# print(response.choices[0].message.content)
client = OpenAI(
    api_key='sk-49248a9a9fe8448f89007c71a3a21600',
    base_url="https://api.deepseek.com")

def call_llm(prompt):
    response = client.chat.completions.create(
        model='deepseek-chat',
        messages=[{'role': 'user', 'content': prompt}],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}})
    return response.choices[0].message.content


# 1. 生成不同思路：3个
question = """
            一个商店卖铅笔，每支2元。如果小明有20元，他最多能买多少支铅笔？
            """

step1_prompt = f"""
                你是一个数学老师。请用3种不同的方法来推理这个问题，只需给出推理思路，不需要解答。思路需要简洁明了，并且合理有效。
                输出格式为：["思路1","思路2","思路3"]
                问题如下：
                {question}
                """

solution_list = call_llm(step1_prompt)
print(f'step1_result->{solution_list}')

# 2.循环遍历每个思路
step2_result_list = []
for solution in eval(solution_list):
    # 将每个思路拼接成一个prompt，分别调用大模型得到结果
    step2_prompt = f"""
                    你是一个数学老师。请用如下的思路来解决这个问题。只输出答案即可。
                    思路：
                    {solution}
                    问题：
                    {question}"""
    step2_result = call_llm(step2_prompt)
    step2_result_list.append(step2_result)
print(f'step2_result_list->{step2_result_list}')

# 3. 每个思路的结果进行投票
step3_prompt = f"""
                你是一个公正的投票专家，能够根据用户输入的list格式的多个答案进行投票，哪个答案出现的次数最多
                你就返回哪个答案，需要注意，返回的答案只需要有计算结果就行，不要有过程。
                用户输入的多个答案：
                {step2_result_list}
                """

step3_result = call_llm(step3_prompt)

print(f'step3_result->{step3_result}')