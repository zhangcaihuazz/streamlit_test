import streamlit as st

# 最简化的页面配置，不使用任何自定义CSS
st.set_page_config(
    page_title="极简测试",
    page_icon="🔍",
    layout="centered"
)

st.title("极简测试页面")
st.write("这个页面只使用最基本的Streamlit组件")

# 测试基本组件
st.write("1. 基本文本显示 - 正常")
st.info("2. 信息框 - 正常")

# 测试输入组件
name = st.text_input("3. 文本输入框")
if name:
    st.write(f"你好，{name}")

# 测试按钮
if st.button("4. 测试按钮"):
    st.success("按钮工作正常！")

st.write("5. 页面加载完成")