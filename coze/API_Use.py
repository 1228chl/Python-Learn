# 从pathlib模块导入Path类，用于处理文件路径
from pathlib import Path
# 从cozepy库导入必要的模块：中国区API地址、客户端主类、消息类、令牌认证类、消息对象类和聊天事件类型
from cozepy import COZE_CN_BASE_URL, Coze, Message, TokenAuth, MessageObjectString, ChatEventType

# 配置部分开始
# API访问令牌，用于身份验证
coze_api_token = 'pat_Fi2fJQKJrPOclXl4pfvwzkQCQ1S8Ubq4QSFjp8mkSwP6gl9j2Kea96HjE0yk8iDx'
# 要调用的机器人ID
bot_id = "7639649026174173194"
# 用户标识符，可以自定义，用于区分不同用户
user_id = "12345"
# 结果保存的本地文件路径（Markdown格式）
RESULT_PATH = r"result.md"

# 实例化coze
coze = Coze(auth=TokenAuth(coze_api_token),base_url=COZE_CN_BASE_URL)

def resume_qa(url, user_prompt):
    """
    调用coze中的面试助手机器人，上传文件，输入问题，返回结果
    :param url: 上传文件的url
    :param user_prompt: 用户的问题
    :return: 模型返回的评估结果
    """

    # 1. 上传文件
    file_response = coze.files.upload(file=Path(url))
    # 判断是否上传成功
    if file_response is None:
        print(f"文件{url}没有上传成功！")
        return None

    # 拿到上传的文件id
    file_id = file_response.id


    # 2 将文件和用户问题封装成消息
    message = [
        Message.build_user_question_objects(
            [
                MessageObjectString.build_file(file_id),
                MessageObjectString.build_text(user_prompt)
            ]
        )
    ]

    # 3 创建一个对话流，将消息给到agent
    stream = coze.chat.stream(
        bot_id = bot_id,
        user_id = user_id,
        additional_messages=message
    )

    # 4 循环对话流中的每一个输出，如果输出是新增，就拼接到最终结果中，如果输出是完成了或者失败了，就直接break。
    result_text = ""
    # 对话流中拿出具体的信息
    for s in stream:
        # print(s)
        if s.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
            result_text += s.message.content
        elif s.event in [ChatEventType.CONVERSATION_CHAT_FAILED,
                                 ChatEventType.CONVERSATION_CHAT_COMPLETED]:
            break


    # 5 存储agent输出的最终结果。
    print(result_text)
    with open(RESULT_PATH, "w", encoding="utf-8") as f:
        f.write(result_text)

    return result_text


if __name__ == '__main__':
    url = r"F:/Heima_File/05_智能体开发/02 物料/coze物料/02-简历.docx"
    user_prompt = "帮我分析下简历"

    result_text = resume_qa(url, user_prompt)