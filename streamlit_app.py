import streamlit as st
import subprocess

def run_command(command):
    try:
        # 使用sudo执行命令，前提是无密码sudo配置
        full_command = f"sudo {command}"
        result = subprocess.run(full_command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"  # 返回更详细的错误信息

# Streamlit 应用界面
st.title("Web 终端模拟（Root权限）")
st.write("在弹窗中输入命令，点击执行后将以root权限运行（需无密码sudo配置）。")

# 弹窗输入命令
if st.button("输入命令并执行"):
    command = st.text_input("请输入要执行的命令：", key="cmd_input")
    if command:
        output = run_command(command)
        st.text_area("命令输出:", output, height=300)
    else:
        st.warning("请输入一个命令。")
