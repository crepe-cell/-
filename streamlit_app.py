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
st.title("Bash 终端模拟")
st.write("在下面的输入框中输入 Bash 命令并按 Enter 键执行。")

# 输入框用于输入命令
command = st.text_input("输入命令:", "", key="command_input")

# 使用 session_state 来存储输出
if "output" not in st.session_state:
    st.session_state.output = ""

# 当输入框的内容变化时执行命令
if command:
    output = run_command(command)
    st.session_state.output = output

# 显示命令输出
st.text_area("命令输出:", st.session_state.output, height=300)

# 提示用户输入命令
if not command:
    st.warning("请输入一个命令。")
