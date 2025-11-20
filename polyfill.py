import streamlit.components.v1 as components


def add_mobile_compatibility_polyfills():
    """添加移动端兼容性polyfill"""
    polyfill_js = """
    <script>
    // Polyfill for AbortSignal.timeout - 解决Safari兼容性问题
    if (!AbortSignal.timeout) {
        AbortSignal.timeout = function(ms) {
            const controller = new AbortController();
            setTimeout(() => controller.abort(new DOMException('TimeoutError', 'TimeoutError')), ms);
            return controller.signal;
        };
        console.log('AbortSignal.timeout polyfill 已加载');
    } else {
        console.log('浏览器原生支持 AbortSignal.timeout');
    }

    // 确保基本的Promise和Fetch功能
    if (window.Promise && window.fetch) {
        console.log('Promise和Fetch支持正常');
    }

    // 防止双击缩放
    let lastTouchEnd = 0;
    document.addEventListener('touchend', function (event) {
        const now = (new Date()).getTime();
        if (now - lastTouchEnd <= 300) {
            event.preventDefault();
        }
        lastTouchEnd = now;
    }, false);

    // 检测并报告设备信息
    console.log('用户代理:', navigator.userAgent);
    console.log('视口尺寸:', window.innerWidth, 'x', window.innerHeight);
    console.log('触摸支持:', 'ontouchstart' in window);
    </script>
    """
    components.html(polyfill_js, height=0)


def set_mobile_viewport():
    """设置移动端友好的viewport"""
    mobile_meta = """
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
    /* 移动端通用优化 */
    @media (max-width: 768px) {
        /* 优化容器间距 */
        .main .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }

        /* 防止iOS输入框缩放 */
        .stNumberInput input, 
        .stTextInput input, 
        .stTextArea textarea,
        .stSelectbox select {
            font-size: 16px !important;
        }

        /* 优化按钮触摸目标 */
        .stButton button {
            min-height: 44px;
            padding: 12px 16px;
        }

        /* 优化列布局在移动端 */
        .row-widget.stColumns > div {
            flex-direction: column;
            gap: 0.5rem;
        }

        /* 优化数据表格显示 */
        .dataframe {
            font-size: 14px;
        }

        /* 优化metric卡片 */
        [data-testid="stMetricValue"] {
            font-size: 1.5rem;
        }

        [data-testid="stMetricDelta"] {
            font-size: 0.9rem;
        }
    }

    /* 小屏手机特殊优化 */
    @media (max-width: 480px) {
        .main .block-container {
            padding: 0.5rem;
        }

        h1 {
            font-size: 1.5rem !important;
        }

        h2 {
            font-size: 1.3rem !important;
        }

        h3 {
            font-size: 1.1rem !important;
        }
    }
    </style>
    """
    components.html(mobile_meta, height=0)


def optimize_mobile_forms():
    """优化移动端表单体验"""
    form_js = """
    <script>
    // 优化移动端表单输入
    document.addEventListener('DOMContentLoaded', function() {
        // 为数字输入框添加步进控制
        const numberInputs = document.querySelectorAll('input[type="number"]');
        numberInputs.forEach(input => {
            input.addEventListener('touchstart', function(e) {
                // 防止iOS双击缩放
                e.preventDefault();
            }, { passive: false });
        });

        // 优化选择框
        const selectBoxes = document.querySelectorAll('.stSelectbox select');
        selectBoxes.forEach(select => {
            select.style.fontSize = '16px'; // 防止iOS缩放
        });

        console.log('移动端表单优化已应用');
    });
    </script>
    """
    components.html(form_js, height=0)