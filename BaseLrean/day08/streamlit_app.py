# 1.导包
import streamlit as st
from ollama_utils import get_chat_result

# 2.添加标题
st.title("黑马智聊机器人")
# 3.添加分割线
st.divider()
# 5.添加历史聊天记录messages列表到streamlit的session_state中
if "messages" not in st.session_state:
    # 首次一定没有历史记录列表,那就创建一个空列表
    st.session_state['messages'] = []
    # 把AI的欢迎语,添加到messages列表中
    st.session_state['messages'].append({"role": "assistant", "content": "你好,我是黑马智聊机器人,有什么可以帮助您的吗!"})
# 4.构建ai和用户的聊天窗口
# 4.1 遍历messages列表,首次只有AI的欢迎语,后续就是用户和AI的问答历史所有记录
for message in st.session_state['messages']:
    st.chat_message(message["role"]).write(message["content"])
# 4.2 获取用户输入
prompt = st.chat_input("请输入您的问题:")
# 如果用户有输入,再进行问答(解决了一开始是None的问题)
if prompt:
    st.chat_message("user").write(prompt)
    # 把用户的问题,添加到messages列表中
    st.session_state['messages'].append({"role": "user", "content": prompt})
    # 4.3 获取AI的回复
    # 注意: 此处要根据用户的问题去调用大模型获取答案
    with st.spinner("思考中..."):
        # messages = [{"role": "user", "content": prompt},{},{},{},{},{},{},{},...]
        # 为了避免messages太长,建议获取最近10条历史记录
        result = get_chat_result(st.session_state['messages'][-10:])
    st.chat_message("assistant").write(result)
    # 把AI的回复,添加到messages列表中
    st.session_state['messages'].append({"role": "assistant", "content": result})