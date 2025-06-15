import streamlit as st
import subprocess

# 会话状态存储用户名和聊天窗口显示状态
if "username" not in st.session_state:
    st.session_state.username = ""
if "show_chat" not in st.session_state:
    st.session_state.show_chat = False
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

# 用户名输入逻辑
if not st.session_state.username:
    st.write("请输入用户名：")
    username_input = st.text_input("用户名")
    if st.button("确认"):
        if username_input.strip():
            st.session_state.username = username_input.strip()
            st.experimental_rerun()
        else:
            st.warning("用户名不能为空")
else:
    st.title(f"欢迎，{st.session_state.username}！Web 终端模拟")

    # 聊天按钮，带聊天图标
    if st.button("聊天", icon=":speech_balloon:"):
        st.session_state.show_chat = not st.session_state.show_chat

    # 自定义CSS，固定聊天框在左下角，聊天内容左下对齐，滚动条自动到最底部
    st.markdown("""
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
            justify-content: flex-end; /* 内容靠下 */
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
            justify-content: flex-end; /* 消息靠下显示 */
            align-items: flex-start; /* 左对齐 */
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
    """, unsafe_allow_html=True)

    # 显示聊天窗口
    if st.session_state.show_chat:
        chat_container = st.container()
        with chat_container:
            st.markdown('<div class="chat-box">', unsafe_allow_html=True)

            # 聊天消息区
            messages_html = "<div class='chat-messages'>"
            for msg in st.session_state.chat_messages:
                messages_html += f"<div>{msg}</div>"
            messages_html += "</div>"
            st.markdown(messages_html, unsafe_allow_html=True)

            # 聊天输入框
            chat_input = st.text_input("", key="chat_input", placeholder="输入消息并回车发送")
            if chat_input:
                st.session_state.chat_messages.append(f"你说: {chat_input}")
                st.session_state.chat_input = ""  # 清空输入框
                st.experimental_rerun()

            st.markdown('</div>', unsafe_allow_html=True)

    # 命令行输入框（聊天窗口关闭时显示）
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
