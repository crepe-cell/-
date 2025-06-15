import streamlit as st
import subprocess
import sys

# 先升级 pip 和 streamlit（只执行一次，避免重复升级）
if "upgraded" not in st.session_state:
    try:
        # 升级 pip
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        # 升级 streamlit
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "streamlit"], check=True)
        st.session_state.upgraded = True
        st.experimental_rerun()  # 升级后重启应用
    except Exception as e:
        st.error(f"升级失败: {e}")
        st.session_state.upgraded = False

# 主应用逻辑
if "username" not in st.session_state:
    st.session_state.username = ""

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

    if st.button("聊天", icon=":speech_balloon:"):
        st.session_state.show_chat = not st.session_state.get("show_chat", False)

    if st.session_state.get("show_chat", False):
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
            </style>
            """,
            unsafe_allow_html=True,
        )
        if "chat_messages" not in st.session_state:
            st.session_state.chat_messages = []
        st.markdown('<div class="chat-box">', unsafe_allow_html=True)
        messages_html = "<div class='chat-messages'>"
        for msg in st.session_state.chat_messages:
            messages_html += f"<div>{msg}</div>"
        messages_html += "</div>"
        st.markdown(messages_html, unsafe_allow_html=True)
        chat_input = st.text_input("", key="chat_input", placeholder="输入消息并回车发送")
        if chat_input:
            st.session_state.chat_messages.append(f"你说: {chat_input}")
            st.session_state.chat_input = ""
            st.experimental_rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    else:
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
