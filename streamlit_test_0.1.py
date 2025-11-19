import streamlit as st

# 绝对最简配置
st.set_page_config(
    page_title="移动端诊断",
    layout="centered"
)

st.title("移动端诊断页面")

# 测试1: 纯文本
st.write("这是纯文本")

# 测试2: 不使用任何列布局
st.write("不使用列布局")

# 测试3: 不使用任何自定义导入
st.success("不使用自定义模块")

# 测试4: 不使用任何表单
st.info("不使用表单")

# 测试5: 只使用最基本组件
if st.button("测试按钮"):
    st.write("按钮被点击了！")

st.write("页面结束")