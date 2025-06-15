import streamlit as st
import subprocess

# 首次输入用户名弹窗
if "username" not in st.session_state:
    st.session_state.username = None

if st.session_state.username is None:
    with st.modal("请输入用户名", True):
        username_input = st.text_input("用户名:", key="username_input")
        if st.button("确认"):
            if username_input.strip():
                st.session_state.username = username_input.strip()
                st.experimental_rerun()
            else:
                st.warning("用户名不能为空")

if st.session_state.username:
    # 顶部居中标题和聊天按钮
    st.markdown(
        """
        <style>
        .header-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            margin-top: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    st.title(f"欢迎，{st.session_state.username}！Web 终端模拟")
    if st.button("聊天", icon=":speech_balloon:"):
        st.session_state.show_chat = not st.session_state.get("show_chat", False)
    st.markdown('</div>', unsafe_allow_html=True)

    # 聊天窗口样式及显示
    st.markdown(
        """
        <style>
        .chat-box {
            position: fixed;
            bottom: 20px;
            left: 20px;
            width: 320px;
            height: 400px;
            background-color: #f0f2f6;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            overflow-y: auto;
            z-index: 9999;
            font-family: Arial, sans-serif;
            font-size: 14px;
        }
        .chat-messages {
            flex-grow: 1;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            align-items: flex-start;
            margin-bottom: 10px;
        }
        .chat-input {
            width: 100%;
            box-sizing: border-box;
            padding: 6px 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if st.session_state.get("show_chat", False):
        if "chat_messages" not in st.session_state:
            st.session_state.chat_messages = []
        chat_container = st.container()
        with chat_container:
            st.markdown('<div class="chat-box">', unsafe_allow_html=True)

            # 显示聊天消息
            messages_html = "<div class='chat-messages'>"
            for msg in st.session_state.chat_messages:
                messages_html += f"<div>{msg}</div>"
            messages_html += "</div>"
            st.markdown(messages_html, unsafe_allow_html=True)

            # 聊天输入框
            chat_input = st.text_input("", key="chat_input", placeholder="输入消息并回车发送")
            if chat_input:
                st.session_state.chat_messages.append(f"你说: {chat_input}")
                st.session_state.chat_input = ""
                st.experimental_rerun()

            st.markdown('</div>', unsafe_allow_html=True)
    else:
        # 命令行输入框，支持回车执行
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
