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
st.write("点击下方按钮开始聊天。")

# 创建一个聊天框
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 聊天输入框
def send_message():
    if st.session_state.input_text:
        command = st.session_state.input_text
        output = run_command(command)
        st.session_state.messages.append({"user": command, "bot": output})
        st.session_state.input_text = ""

# 悬浮窗聊天按钮
if st.button("聊天"):
    st.text_input("输入命令:", key="input_text", on_change=send_message)

# 显示聊天记录
for message in st.session_state.messages:
    st.write(f"**你:** {message['user']}")
    st.write(f"**输出:** {message['bot']}")

# 提示用户使用 Enter 键发送消息
st.write("按 Enter 键发送消息。")
