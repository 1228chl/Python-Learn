import streamlit as st
from datetime import date

from docutils.nodes import label


# 设置页面标题
st.title("传智教育用户注册平台")

# 添加分隔线
st.divider()

# 用户名输入框
username = st.text_input(label="请输入用户名",max_chars=50,key="username")

# 密码输入框
password = st.text_input(label="请输入密码",type="password",max_chars=50,key="password")

# 年龄输入框
age = st.number_input(
    label="年龄",
    min_value=0,
    max_value=200,
    step=1,
    key="age"
)

# 性别选择框
gender = st.selectbox(
    label="性别",
    options=["请选择。。。","男","女","妖"],
    index=0,
    key="gender"
)

# 是否已婚单选框
st.radio(
    label="是否已婚",
    options=["是","否"],
    index=1,
    horizontal=True,
    key="married"
)

# 出生日期选择器
birthdate = st.date_input(
    label='出生日期',
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    key='birthdate')

# 身高输入框
height = st.slider(
    label='身高',
    min_value=40.0,
    max_value=300.0,
    value=175.0,
    step=0.1,
    key='height')

# 提交按钮
submit_button = st.button(label='注册')

# 处理表单提交
if submit_button:
    st.success(f"注册成功")
    st.write(f"注册成功！以下是您的信息:\n用户名: {username}\n密码: {password}\n年龄: {age}\n性别: {gender}\n出生日期: {birthdate}\n身高: {height} cm")