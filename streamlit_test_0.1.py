import streamlit as st

st.set_page_config(
    page_title="简单测试",
    page_icon="✅",
    layout="centered"
)

# 最简单的移动端适配
st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body {
    font-family: Arial, sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 简单测试页面")
st.write("如果这个页面能在手机上正常显示，说明部署环境正常")

st.success("✅ 这是一个成功消息")
st.error("❌ 这是一个错误消息")
st.warning("⚠️ 这是一个警告消息")

st.write("---")

# 一些简单的交互元素
name = st.text_input("请输入您的名字", placeholder="例如：张三")
if name:
    st.write(f"你好，{name}！")

number = st.number_input("请输入一个数字", min_value=0, max_value=100, value=50)
st.write(f"您输入的数字是: {number}")

if st.button("点击测试"):
    st.balloons()
    st.success("按钮点击成功！")

st.write("---")
st.info("如果这个简单页面在手机上能正常显示，那么问题出在您的应用代码中。如果不能显示，则是部署环境的问题。")