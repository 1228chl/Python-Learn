
import time
from datetime import datetime
from openai import OpenAI


# 设置你的 DashScope API Key
# dashscope.api_key = os.getenv("api_key")


# 工具1：获取当前日期（返回格式：YYYY年MM月DD日）
def get_current_date():
    """返回当前日期，格式：2025年9月15日"""
    now = datetime.now()
    return f"{now.year}年{now.month}月{now.day}日"


# 工具2：查询节假日（根据月份查询）
def search_holidays(month):
    """
    查询指定月份的法定节假日
    month: 月份字符串，如 "9月"
    """
    # 模拟节假日数据
    holidays = {
        "1月": ["元旦：1月1日"],
        "2月": ["春节：1月28日-2月3日"],
        "3月": [],
        "4月": ["清明节：4月4日-6日"],
        "5月": ["劳动节：5月1日-5日", "端午节：5月31日-6月2日"],
        "6月": [],
        "7月": [],
        "8月": [],
        "9月": [],  # 2025年9月没有法定节假日
        "10月": ["中秋节：10月6日-8日", "国庆节：10月1日-7日"],
        "11月": [],
        "12月": ["元旦：12月31日"]
    }

    # 获取指定月份的节假日
    holidays_list = holidays.get(month, [])

    if holidays_list:
        return f"2025年{month}有以下法定节假日：\n" + "\n".join(holidays_list)
    else:
        return f"2025年{month}没有法定节假日。"


# 工具注册
TOOLS = {
    "get_current_date": get_current_date,
    "search_holidays": search_holidays
}
client = OpenAI(
    api_key='sk-49248a9a9fe8448f89007c71a3a21600',
    base_url="https://api.deepseek.com")

# 调用Qwen模型
def call_qwen(prompt):
    response = client.chat.completions.create(
        model='deepseek-chat',
        messages=[{'role': 'user', 'content': prompt}],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}})
    return response.choices[0].message.content


# 解析模型输出
def parse_model_output(output):
    """
    解析模型输出，提取 Thought, Action, Action Input
    不使用正则表达式，使用简单的字符串处理
    """
    thought = ""
    action = ""
    action_input = ""

    lines = output.split('\n')

    for line in lines:
        line = line.strip()
        if line.startswith('Thought:'):
            thought = line.replace('Thought:', '').strip()
        elif line.startswith('Action:'):
            action = line.replace('Action:', '').strip()
        elif line.startswith('Action Input:'):
            action_input = line.replace('Action Input:', '').strip()

    return thought, action, action_input


# 从输入中提取月份信息
def extract_month(text):
    """
    从文本中提取月份信息，如 "9月"
    """
    # 检查常见的月份表示方式
    months = ["1月", "2月", "3月", "4月", "5月", "6月",
              "7月", "8月", "9月", "10月", "11月", "12月"]

    for month in months:
        if month in text:
            return month

    # 如果没有找到明确的月份，返回当前月份
    current_month = datetime.now().month
    return f"{current_month}月"


# ReAct主循环
def react_solve(question):
    print(f"问题：{question}\n")
    steps = []  # 用来存储每一步的输出
    max_iterations = 5
    print("开始ReAct推理流程...\n")

    for i in range(max_iterations):
        # 构建上下文（包含之前的所有步骤）
        context = "\n".join(steps)
        prompt = f"""
                    你是一个使用ReAct范式的智能代理，必须严格按以下格式输出：
                    Thought: <你的思考>
                    Action: <要执行的动作，从 [{', '.join(TOOLS.keys())}] 中选择，或 Final Answer>
                    Action Input: <动作输入>

                    当前上下文：
                    {context}

                    问题：{question}
                    """

        # 调用Qwen生成下一步
        output = call_qwen(prompt)
        print(f"模型输出（第{i + 1}步）：\n{output}\n")

        # 解析输出
        thought, action, action_input = parse_model_output(output)

        # 检查解析结果
        if not thought or not action:
            steps.append(f"Error: 无法解析输出格式。输出: {output}")
            print("解析失败，继续尝试...\n")
            continue

        # 记录历史步骤
        steps.append(f"Thought: {thought}")
        steps.append(f"Action: {action}")

        # 如果是最终答案
        if action == "Final Answer":
            print("任务完成！最终答案：")
            print(f"   {action_input}\n")
            return action_input

        # 执行工具
        if action in TOOLS:
            print(f"执行工具: {action} | 输入: {action_input}")
            # try:
            # 传递参数给工具
            if action == "search_holidays":
                # 使用新的月份提取方法
                month = extract_month(action_input)
                result = TOOLS[action](month)
            else:
                result = TOOLS[action]()

            steps.append(f"Action Input: {action_input}")
            steps.append(f"Observation: {result}")
            print(f"Observation: {result}\n")
            time.sleep(0.5)  # 避免频繁调用
        else:
            result = f"无效动作: {action}"
            steps.append(f"Action Input: {action_input}")
            steps.append(f"Observation: {result}")
            print(f"Observation: {result}\n")

    # 超出最大迭代次数
    final_answer = "无法在限定步数内完成任务。"
    print(f"任务失败: {final_answer}")
    return final_answer



# 运行示例
if __name__ == "__main__":
    # 运行主程序
    question = "这个月有几个法定节假日？分别是什么？"
    result = react_solve(question)