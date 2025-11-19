import streamlit as st

# 最简化的页面配置，不使用任何自定义CSS
st.set_page_config(
    page_title="极简测试",
    page_icon="165",
    layout="centered"
)

st.title("极简测试页面")
st.write("这个页面只使用最基本的Streamlit组件")