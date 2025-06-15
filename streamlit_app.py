import streamlit as st
import subprocess

def run_command(command):
    try:
        # 使用shell=True调用系统shell执行命令，捕获stdout和stderr
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        # 返回错误信息，包括stderr
        return f"Error:\n{e.stderr}"

st.title("Bash 终端模拟")

# 使用文本输入框，支持输入单行命令
command = st.text_input("输入 Bash 命令:")

# 当用户按下 Enter 键时执行命令
if command.strip():
    output = run_command(command)
    st.text_area("命令输出:", output, height=300)
else:
    st.warning("请输入命令。")
