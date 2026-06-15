import os
import streamlit as st
# 使用
st.title('Streamlit测试页面')
text = st.text_input("请您输入文本：\n")
if text:
    st.write(f"您输入的文本是：{text}")# 写到页面
    print(f"您输入的文本是：{text}")# 控制台输出

os.system(r"streamlit run G:\code\python\Python-Learn\Project\SubmitAFullScoreProject\test\回顾streamlit入门使用.py")

