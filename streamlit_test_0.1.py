import streamlit as st

# 极简配置，避免任何可能导致问题的设置
st.set_page_config(
    page_title="血糖胰岛素控制程序",
    page_icon="🩸",
    layout="centered",
    initial_sidebar_state="auto"
)


# 完全避免使用 st.markdown 注入 HTML/CSS
# 使用纯 Streamlit 组件

def main():
    st.header("血糖胰岛素控制程序 Beta 0.0.1")

    # 使用容器确保内容正确渲染
    with st.container():
        st.subheader("当前系统状态")

        # 使用列布局但简化
        col1, col2, col3 = st.columns(3)

        with col1:
            try:
                from utils.file_utils import load_json
                rsi_data = load_json('rsi_data.json')
                if rsi_data:
                    st.success(f"RSI: {rsi_data.get('rsi_value', 'N/A')}")
                else:
                    st.error("RSI: 未校准")
            except:
                st.error("RSI: 加载失败")

        with col2:
            try:
                from utils.file_utils import load_json
                isf_data = load_json('isf_data.json')
                if isf_data:
                    st.success(f"ISF: {isf_data.get('isf_value', 'N/A')}")
                else:
                    st.error("ISF: 未校准")
            except:
                st.error("ISF: 加载失败")

        with col3:
            try:
                from utils.file_utils import load_json
                food_data = load_json('foods_data.json')
                if food_data:
                    st.success(f"食物: {len(food_data)}种")
                else:
                    st.warning("食物: 0种")
            except:
                st.warning("食物: 加载失败")

    # 添加简单的导航
    st.write("---")
    st.write("功能页面:")

    # 使用按钮而不是链接
    if st.button("📝 食物信息录入"):
        st.switch_page("pages/page_food_input.py")

    if st.button("📊 RSI校准"):
        st.switch_page("pages/page_rsi_calibration.py")

    if st.button("⚙️ ISF校准"):
        st.switch_page("pages/page_isf_calibration.py")

    if st.button("💉 胰岛素计算"):
        st.switch_page("pages/Page_insulin_calculation.py")


if __name__ == "__main__":
    main()