import streamlit as st
import subprocess

def run_command(command):
    try:
        full_command = f"sudo {command}"
        result = subprocess.run(full_command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.strip()}"

st.title("Web 终端模拟（Root权限）")
st.write("在输入框中输入命令，按回车或点击执行按钮将以root权限运行（需无密码sudo配置）。")

with st.form(key='command_form'):
    command = st.text_input("请输入要执行的命令：")
    submit_button = st.form_submit_button(label='执行')

if submit_button:
    if command:
        output = run_command(command)
        st.text_area("命令输出:", output, height=300)
    else:
        st.warning("请输入一个命令。")
