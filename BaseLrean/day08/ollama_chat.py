import streamlit as st
from ollama_utils import get_chat_result

# 创建一个聊天机器人标题
st.title("黑马聊天机器人")
# 实现分割线
st.divider()

# 在会话状态模块中添加一个messages的列表，用来存储会话内容
if "messages" not in st.session_state:
    st.session_state.messages = []
    # 添加一个系统提示（系统提示词）
    st.session_state.messages.append({"role":"assistant","content":"我是黑马智聊机器人，可以开始提问了"})

# 显示所有对话的聊天历史
for message in st.session_state.messages:#遍历会话内容
    with st.chat_message(name=message["role"]):# name属性：会话角色名称
        st.write(message["content"])
# 实现用户输入框
# placeholder：输入和提示语
prompt = st.chat_input(placeholder="请输入你的问题:")
# 判断用户输入框是否为空
if prompt:
    # 实现用户提问展示
    with st.chat_message("user"):
        st.write(prompt)
        # 组织用户输入的字典格式会话内容
        user_message = {"role":"user","content":prompt}
        # 添加用户输入的会话内容到历史会话中
    st.session_state.messages.append(user_message)
    # 调用ollama后缀大模型会话函数获取大模型会话结果
    response = get_chat_result([user_message])
    #实现AI大模型回答展示
    with st.chat_message("assistant"):
        st.write(response)
    st.session_state.messages.append({"role":"assistant","content":response})