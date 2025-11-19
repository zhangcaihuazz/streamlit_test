import streamlit as st

# 设置页面标题
st.set_page_config(page_title="Streamlit 测试应用", layout="centered")

# 显示标题
st.title("欢迎使用 Streamlit!")

# 显示一段文本
st.write("这是一个测试应用，用来确认在手机和桌面端的表现。")

# 添加一个按钮
if st.button('点击我'):
    st.write("你点击了按钮！")

# 显示文本输入框
name = st.text_input("请输入你的名字：")
if name:
    st.write(f"你好，{name}！")
