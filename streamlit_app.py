import streamlit as st
import subprocess

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

    if st.button("ChatUI"):
        st.write("开始与伙伴聊天...")
        chat_input = st.text_input("输入消息并回车发送", key="chat_input")
        if chat_input:
            st.write(f"你说: {chat_input}")
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
