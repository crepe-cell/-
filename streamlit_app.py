import streamlit as st
import subprocess

# 初始化会话状态
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def run_command(command):
    try:
        # 执行命令并捕获输出
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

# Streamlit 应用
st.title("Web 终端模拟")
st.write("欢迎使用 Web 终端！请先输入您的名称。")

# 用户自定义名称
if st.session_state.username == "":
    st.session_state.username = st.text_input("请输入您的名称:", "")
else:
    # 显示聊天历史
    for entry in st.session_state.chat_history:
        st.text(entry)

    # 输入框用于输入命令
    command = st.text_input("输入命令并按 Enter 执行:", "")

    if command:
        output = run_command(command)
        st.session_state.chat_history.append(f"{st.session_state.username}: {command}")
        st.session_state.chat_history.append(f"输出: {output}")
        st.experimental_rerun()  # 重新运行以更新聊天历史

# 显示聊天框
if st.session_state.username:
    st.text_area("聊天记录:", "\n".join(st.session_state.chat_history), height=300, disabled=True)
