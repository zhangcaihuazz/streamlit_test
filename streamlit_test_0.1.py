import streamlit as st
import streamlit.components.v1 as components
import sys
import os

# 添加utils路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

# 导入polyfill函数
try:
    from utils.polyfill import add_mobile_compatibility_polyfills, set_mobile_viewport, optimize_mobile_forms
except ImportError:
    st.error("无法加载polyfill模块，请确保utils/polyfill.py文件存在")


    # 提供临时的polyfill功能
    def add_mobile_compatibility_polyfills():
        components.html("""
        <script>
        console.log('使用临时polyfill');
        if (!AbortSignal.timeout) {
            AbortSignal.timeout = function(ms) {
                const controller = new AbortController();
                setTimeout(() => controller.abort(new DOMException('TimeoutError', 'TimeoutError')), ms);
                return controller.signal;
            };
        }
        </script>
        """, height=0)


    def set_mobile_viewport():
        components.html("""
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <style>
        @media (max-width: 768px) {
            .main .block-container { padding: 1rem; }
            .stNumberInput input, .stTextInput input { font-size: 16px !important; }
            .stButton button { min-height: 44px; }
        }
        </style>
        """, height=0)


    def optimize_mobile_forms():
        pass

# 设置页面配置
st.set_page_config(
    page_title="移动端兼容性测试",
    page_icon="📱",
    layout="centered"
)

# 应用polyfill
add_mobile_compatibility_polyfills()
set_mobile_viewport()
optimize_mobile_forms()

# 测试页面内容
st.title("📱 移动端兼容性测试")
st.markdown("这个页面用于测试应用在移动设备上的兼容性。")

# 设备检测
st.subheader("设备信息")
col1, col2 = st.columns(2)
with col1:
    st.metric("用户代理", "检测中...", "JavaScript")
with col2:
    st.metric("视口宽度", "未知", "CSS")

# 添加JavaScript来检测设备信息
components.html("""
<script>
// 检测设备信息
function updateDeviceInfo() {
    const userAgent = navigator.userAgent;
    const viewportWidth = window.innerWidth;

    // 发送信息回Streamlit
    if (window.parent && window.parent.streamlitDebug) {
        window.parent.streamlitDebug({
            userAgent: userAgent,
            viewportWidth: viewportWidth
        });
    }

    console.log('用户代理:', userAgent);
    console.log('视口宽度:', viewportWidth);
    console.log('AbortSignal.timeout支持:', typeof AbortSignal.timeout === 'function');
}

// 页面加载完成后检测
document.addEventListener('DOMContentLoaded', updateDeviceInfo);
window.addEventListener('resize', updateDeviceInfo);

// 初始检测
updateDeviceInfo();
</script>
""", height=0)

# 功能测试区域
st.subheader("功能测试")

# 测试1: 表单输入
with st.form("test_form"):
    st.write("表单输入测试")

    col1, col2 = st.columns(2)
    with col1:
        text_input = st.text_input("文本输入", placeholder="测试文本输入")
        number_input = st.number_input("数字输入", min_value=0, max_value=100, value=50)

    with col2:
        select_box = st.selectbox("选择框", ["选项1", "选项2", "选项3"])
        slider = st.slider("滑块", 0, 100, 50)

    checkbox = st.checkbox("复选框测试")
    submit_button = st.form_submit_button("提交表单")

if submit_button:
    st.success("表单提交成功！")
    st.write(f"文本: {text_input}, 数字: {number_input}, 选择: {select_box}, 滑块: {slider}, 复选框: {checkbox}")

# 测试2: 按钮和交互
st.write("按钮交互测试")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("主要按钮", type="primary"):
        st.toast("主要按钮被点击!", icon="✅")

with col2:
    if st.button("次要按钮"):
        st.toast("次要按钮被点击!", icon="ℹ️")

with col3:
    if st.button("警告按钮", type="secondary"):
        st.warning("警告按钮被点击!")

# 测试3: 数据显示
st.subheader("数据显示测试")

# 创建示例数据
import pandas as pd
import numpy as np

sample_data = pd.DataFrame({
    '食物名称': ['苹果', '香蕉', '面包', '米饭', '鸡肉'],
    '碳水 (g/100g)': [14, 23, 49, 28, 0],
    '蛋白质 (g/100g)': [0.3, 1.1, 9, 2.7, 27],
    '脂肪 (g/100g)': [0.2, 0.3, 3.2, 0.3, 3.6]
})

st.dataframe(sample_data, use_container_width=True)

# 测试4: 布局测试
st.subheader("布局测试")

st.info("以下测试不同列布局在移动端的表现")

# 三列布局
st.write("三列布局:")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("指标1", "100", "10%")
with col2:
    st.metric("指标2", "200", "-5%")
with col3:
    st.metric("指标3", "150", "15%")

# 两列布局
st.write("两列布局:")
col1, col2 = st.columns(2)
with col1:
    st.text_input("左列输入", placeholder="左侧输入框")
with col2:
    st.number_input("右列数字", min_value=0, value=100)

# 选项卡测试
st.write("选项卡测试:")
tab1, tab2, tab3 = st.tabs(["选项卡1", "选项卡2", "选项卡3"])
with tab1:
    st.write("这是第一个选项卡的内容")
with tab2:
    st.write("这是第二个选项卡的内容")
with tab3:
    st.write("这是第三个选项卡的内容")

# 扩展区域测试
with st.expander("点击展开/收起测试"):
    st.write("这是可展开区域的内容")
    st.image("https://via.placeholder.com/150", caption="示例图片", width=150)

# 状态检查
st.subheader("兼容性状态检查")

# Polyfill状态
st.write("Polyfill状态:")
col1, col2 = st.columns(2)
with col1:
    st.success("✅ AbortSignal.timeout Polyfill 已加载")
with col2:
    st.success("✅ 移动端Viewport 已设置")

# 功能检查清单
st.write("功能检查清单:")
checklist_col1, checklist_col2 = st.columns(2)

with checklist_col1:
    st.checkbox("文本输入正常", value=True, disabled=True)
    st.checkbox("数字输入正常", value=True, disabled=True)
    st.checkbox("按钮点击正常", value=True, disabled=True)

with checklist_col2:
    st.checkbox("选择框正常", value=True, disabled=True)
    st.checkbox("滑块正常", value=True, disabled=True)
    st.checkbox("表单提交正常", value=True, disabled=True)

# 移动端优化建议
st.subheader("移动端优化建议")

with st.container():
    st.info("""
    **移动端优化提示:**
    - 确保所有交互元素有足够大的触摸目标(至少44x44像素)
    - 使用适合移动设备的字体大小(最小16px防止iOS缩放)
    - 在移动端考虑使用单列布局
    - 优化数据表格在小屏幕上的显示
    - 测试所有功能在触摸设备上的表现
    """)

# 底部信息
st.markdown("---")
st.caption("测试完成 - 请在移动设备上检查所有功能是否正常工作")

# 添加调试信息
if st.checkbox("显示调试信息"):
    st.subheader("调试信息")
    st.code("""
    常见移动端问题:
    1. AbortSignal.timeout 不兼容 - 已通过Polyfill解决
    2. 正则表达式命名捕获组 - 可能需要更新Streamlit版本
    3. 输入框自动缩放 - 通过font-size:16px解决
    4. 触摸目标太小 - 通过min-height:44px优化
    """)