import streamlit as st

st.title("黑马聊天机器人")
st.divider()
with st.chat_message("assistant"):
    st.write("欢迎来到黑马程序员，有什么需要帮助的吗？")
    st.write("请输入你的问题:")

st.chat_input(placeholder="请输入你的问题:")

with st.chat_message("user"):
    st.write("黑马程序员是一个好的培训机构吗？")
with st.chat_message("assistant"):
    st.write("黑马程序员是一个很好的培训机构")