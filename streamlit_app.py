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
st.write("在下面的输入框中输入命令并点击执行。")

# 输入框用于输入命令
command = st.text_input("输入命令:", "")

if st.button("执行"):
    if command:
        output = run_command(command)
        st.text_area("命令输出:", output, height=300)
    else:
        st.warning("请输入一个命令。")
