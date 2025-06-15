import streamlit as st
import subprocess

# 初始化会话状态
if "username" not in st.session_state:
    st.session_state.username = ""
if "show_chat" not in st.session_state:
    st.session_state.show_chat = False
if "refresh_flag" not in st.session_state:
    st.session_state.refresh_flag = False  # 用于触发刷新

# 用户名输入逻辑（简易版）
if not st.session_state.username:
    st.write("请输入用户名：")
    username_input = st.text_input("用户名")
    if st.button("确认"):
        if username_input.strip():
            st.session_state.username = username_input.strip()
            # 通过切换refresh_flag触发页面刷新
            st.session_state.refresh_flag = not st.session_state.refresh_flag
            st.experimental_rerun()  # 如果仍报错可注释此行，依赖refresh_flag刷新
        else:
            st.warning("用户名不能为空")
else:
    st.title(f"欢迎，{st.session_state.username}！Web 终端模拟")

    # 聊天按钮，使用聊天气泡图标
    if st.button("聊天", icon=":material/chat:"):
        st.session_state.show_chat = not st.session_state.show_chat

    # 聊天窗口左下角固定样式
    st.markdown(
        """
        <style>
        .chat-box {
            position: fixed;
            bottom: 20px;
            left: 20px;
            width: 300px;
            height: 400px;
            background-color: #f0f2f6;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 10px;
            overflow-y: auto;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            z-index: 9999;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # 显示聊天窗口
    if st.session_state.show_chat:
        chat_container = st.container()
        with chat_container:
            st.markdown('<div class="chat-box">', unsafe_allow_html=True)
            st.write("💬 伙伴聊天开始了！")
            chat_input = st.text_input("输入消息并回车发送", key="chat_input")
            if chat_input:
                st.write(f"你说: {chat_input}")
            st.markdown('</div>', unsafe_allow_html=True)

    # 命令行输入框
    if not st.session_state.show_chat:
        command = st.text_input("输入命令并按 Enter 执行:", key="command_input")
        if command:
            def run_command(command):
                try:
                    result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
                    return result.stdout
                except subprocess.CalledProcessError as e:
                    return f"Error: {e}"
            output = run_command(command)
            st.text_area("命令输出:", output, height=300)
