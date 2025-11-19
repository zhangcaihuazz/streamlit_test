"""
血糖胰岛素控制程序 - 主应用入口文件
版本: Beta 0.0.1
功能: 显示血糖胰岛素控制系统的当前状态仪表板
"""
#streamlit run bloodsugar_app_0.0.1beta.py

# 导入必要的Python标准库模块
import streamlit as st  # 用于构建Web应用的Python框架
import sys  # 提供对Python解释器相关功能的访问
import os  # 提供与操作系统交互的功能

# 添加自定义模块路径到Python路径中
# 这样Python解释器能够找到我们自定义的模块文件
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))  # 添加modules文件夹路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))  # 添加utils文件夹路径

# 设置Streamlit页面配置 - 必须在任何st.调用之前
st.set_page_config(
    page_title="血糖胰岛素控制程序",  # 浏览器标签页显示的标题
    page_icon="🩸",  # 浏览器标签页显示的图标（血液emoji）
    layout="centered",  # 改为centered布局，更适合移动端
    initial_sidebar_state="collapsed"  # 移动端默认收起侧边栏
)

# 强制移动端适配的CSS - 放在最前面
st.markdown("""
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
    /* 基础重置确保兼容性 */
    html, body, [class*="css"]  {
        font-family: 'Source Sans Pro', sans-serif;
    }
    
    /* 移动端适配 */
    @media (max-width: 768px) {
        /* 主容器调整 */
        .main .block-container {
            padding-top: 1rem !important;
            padding-bottom: 1rem !important;
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
            max-width: 100% !important;
        }
        
        /* 标题调整 */
        h1, h2, h3 {
            font-size: 1.2rem !important;
            text-align: center;
        }
        
        /* 列布局在移动端改为垂直 */
        .row-widget.stColumns {
            flex-direction: column !important;
        }
        
        .row-widget.stColumns > div {
            width: 100% !important;
            margin-bottom: 1rem;
        }
        
        /* 按钮全宽度 */
        .stButton > button {
            width: 100% !important;
            min-height: 3rem;
            font-size: 1rem;
        }
        
        /* 输入框调整 */
        .stTextInput input, .stNumberInput input, .stSelectbox select {
            font-size: 16px !important; /* 防止iOS缩放 */
            height: 3rem !important;
        }
        
        /* 状态卡片调整 */
        [data-testid="stMetricValue"] {
            font-size: 1.5rem !important;
        }
        
        [data-testid="stMetricLabel"] {
            font-size: 0.9rem !important;
        }
        
        /* 隐藏不必要的元素 */
        .stAppHeader {
            display: none !important;
        }
    }
    
    /* 通用样式确保内容可见 */
    .stApp {
        background-color: white;
    }
    
    /* 确保内容区域可见 */
    .main {
        background-color: white;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    """
    主应用入口函数

    功能:
    - 显示应用标题
    - 调用状态显示函数展示当前系统状态
    """
    # 应用主标题 - 添加容器确保可见
    with st.container():
        st.header("🧊 水晶能量计算器 Beta 0.0.1")  # 显示带图标的标题

    # 显示当前系统状态
    show_current_status()


def show_current_status():
    """
    显示当前系统状态信息

    功能:
    - 从JSON文件加载RSI（胰岛素敏感系数）数据
    - 从JSON文件加载ISF（胰岛素敏感因子）数据
    - 从JSON文件加载食物数据库数据
    - 使用三列布局展示各项状态信息
    - 处理数据加载异常情况

    异常处理:
    - 捕获数据加载过程中的所有异常
    - 显示友好的错误信息给用户
    """

    try:
        # 从utils模块导入JSON文件加载功能
        from utils.file_utils import load_json

        # 创建子标题
        st.subheader("📊 当前系统状态")

        # 在移动端使用垂直布局，桌面端使用水平布局
        if check_mobile():
            # 移动端垂直布局
            st.info("📱 移动端模式")

            with st.container():
                # RSI状态
                rsi_data = load_json('rsi_data.json')
                if rsi_data:
                    st.success(f"**RSI值**: {rsi_data['rsi_value']}")
                    if 'timestamp' in rsi_data:
                        st.caption(f"最后更新: {rsi_data['timestamp']}")
                else:
                    st.error("**RSI值**: 未校准")
                    st.caption("请先进行RSI校准")

                # ISF状态
                isf_data = load_json('isf_data.json')
                if isf_data:
                    st.success(f"**ISF值**: {isf_data['isf_value']} mmol/L/U")
                    if 'timestamp' in isf_data:
                        st.caption(f"最后更新: {isf_data['timestamp']}")
                else:
                    st.error("**ISF值**: 未校准")
                    st.caption("请先进行ISF校准")

                # 食物数据状态
                food_data = load_json('foods_data.json')
                if food_data:
                    st.success(f"**食物数据**: {len(food_data)} 种")
                    recent_foods = food_data[-3:] if len(food_data) >= 3 else food_data
                    food_list = "  ".join([f"• {food['name']}" for food in recent_foods])
                    st.caption(f"最近录入: {food_list}")
                else:
                    st.warning("**食物数据**: 0 种")
                    st.caption("请先录入食物信息")
        else:
            # 桌面端水平布局
            col1, col2, col3 = st.columns(3)

            with col1:
                rsi_data = load_json('rsi_data.json')
                if rsi_data:
                    st.success(f"**RSI值**: {rsi_data['rsi_value']}")
                    if 'timestamp' in rsi_data:
                        st.caption(f"最后更新: {rsi_data['timestamp']}")
                else:
                    st.error("**RSI值**: 未校准")
                    st.caption("请先进行RSI校准")

            with col2:
                isf_data = load_json('isf_data.json')
                if isf_data:
                    st.success(f"**ISF值**: {isf_data['isf_value']} mmol/L/U")
                    if 'timestamp' in isf_data:
                        st.caption(f"最后更新: {isf_data['timestamp']}")
                else:
                    st.error("**ISF值**: 未校准")
                    st.caption("请先进行ISF校准")

            with col3:
                food_data = load_json('foods_data.json')
                if food_data:
                    st.success(f"**食物数据**: {len(food_data)} 种")
                    recent_foods = food_data[-3:]
                    food_list = "\n".join([f"• {food['name']}" for food in recent_foods])
                    st.caption(f"最近录入:\n{food_list}")
                else:
                    st.warning("**食物数据**: 0 种")
                    st.caption("请先录入食物信息")

    except Exception as e:
        # 显示通用错误信息
        st.error("❌ 数据加载错误")
        # 显示具体的错误信息
        st.info(f"错误详情: {str(e)}")
        # 提供调试建议
        st.warning("💡 如果持续出现此错误，请检查数据文件是否存在且格式正确")


def check_mobile():
    """
    简单的移动设备检测
    在实际部署中，这可以通过用户代理检测实现
    这里我们使用一个简化的版本
    """
    try:
        # 这里可以添加更复杂的移动设备检测逻辑
        # 暂时返回False，让CSS来处理响应式布局
        return False
    except:
        return False


# Python程序的入口点
if __name__ == "__main__":
    main()