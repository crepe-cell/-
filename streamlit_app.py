import streamlit as st
import subprocess
import os
import pty

def run_bash_command(command):
    try:
        # 使用 pty 创建伪终端
        master, slave = pty.openpty()
        process = subprocess.Popen(
            ['/bin/bash'], 
            stdin=slave, 
            stdout=slave, 
            stderr=slave, 
            text=True
        )
        os.close(slave)

        # 向 Bash 发送命令
        os.write(master, (command + '\n').encode())

        output = ''
        while True:
            # 读取输出
            try:
                data = os.read(master, 1024).decode()
                if not data:
                    break
                output += data
            except OSError:
                break

        process.wait()  # 等待进程结束
        return output
    except Exception as e:
        return f"Error: {e}"

# Streamlit 应用
st.title("Bash 终端模拟")
st.write("在下面的输入框中输入 Bash 命令并按 Enter 键执行。")

# 输入框用于输入命令
command = st.text_input("输入命令:", "", key="command_input")

# 使用 session_state 来存储输出
if st.session_state.get("output") is None:
    st.session_state.output = ""

# 当输入框的内容变化时执行命令
if command:
    output = run_bash_command(command)
    st.session_state.output = output

# 显示命令输出
st.text_area("命令输出:", st.session_state.output, height=300)

# 提示用户输入命令
if not command:
    st.warning("请输入一个命令。")
