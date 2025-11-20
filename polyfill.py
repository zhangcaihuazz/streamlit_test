import streamlit.components.v1 as components


def add_mobile_compatibility_polyfills():
    """添加移动端兼容性polyfill"""
    polyfill_js = """
    <script>
    // Polyfill for AbortSignal.timeout
    if (!AbortSignal.timeout) {
        AbortSignal.timeout = function(ms) {
            const controller = new AbortController();
            setTimeout(() => controller.abort(new DOMException('TimeoutError', 'TimeoutError')), ms);
            return controller.signal;
        };
    }

    // 确保基本的Promise和Fetch功能
    if (window.Promise && window.fetch) {
        console.log('Polyfills loaded successfully');
    }
    </script>
    """
    components.html(polyfill_js, height=0)


def set_mobile_viewport():
    """设置移动端友好的viewport"""
    mobile_meta = """
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <style>
    @media (max-width: 768px) {
        /* 移动端样式优化 */
        .main .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }

        /* 确保输入框在移动端可正常使用 */
        .stNumberInput input, .stTextInput input {
            font-size: 16px !important; /* 防止iOS缩放 */
        }
    }
    </style>
    """
    components.html(mobile_meta, height=0)