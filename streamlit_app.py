import streamlit as st
import subprocess

def run_command(command):
    try:
        # 执行命令并捕获输出
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

# Streamlit 应用
st.title("Web 终端模拟")

# 创建一个聊天框
if 'messages' not in st.session_state:
    st.session_state.messages = []
    st.session_state.user_name = ""

# 提示用户输入名称
if st.session_state.user_name == "":
    st.session_state.user_name = st.text_input("请输入您的名称:", "")
    if st.session_state.user_name:
        st.success(f"欢迎，{st.session_state.user_name}！请点击下方按钮开始聊天。")

# 聊天输入框和按钮
if st.button("聊天"):
    # 显示输入框
    command = st.text_input("输入命令:", key="input_text")
    
    # 发送消息的功能
    if command:
        output = run_command(command)
        st.session_state.messages.append({"user": command, "bot": output})
        st.session_state.input_text = ""  # 清空输入框

# 显示聊天记录
if st.session_state.messages:
    for message in st.session_state.messages:
        st.write(f"**{st.session_state.user_name}:** {message['user']}")
        st.write(f"**输出:** {message['bot']}")

# 提示用户使用 Enter 键发送消息
st.write("按 Enter 键发送消息。")
