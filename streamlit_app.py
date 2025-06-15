import streamlit as st
import paramiko

def run_command_via_ssh(host, username, password, command):
    try:
        # 创建 SSH 客户端
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # 连接到远程主机
        client.connect(host, username=username, password=password)
        
        # 执行命令
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode() + stderr.read().decode()
        
        # 关闭连接
        client.close()
        return output
    except Exception as e:
        return f"Error: {e}"

# Streamlit 应用
st.title("SSH 终端模拟")
st.write("在下面的输入框中输入 Bash 命令并按 Enter 键执行。")

# 输入框用于输入命令
command = st.text_input("输入命令:", "", key="command_input")

# SSH 连接信息
host = st.text_input("主机地址:", "sshx.io", key="host_input")
username = st.text_input("用户名:", "", key="username_input")
password = st.text_input("密码:", "", key="password_input", type="password")

# 使用 session_state 来存储输出
if st.session_state.get("output") is None:
    st.session_state.output = ""

# 当输入框的内容变化时执行命令
if command and host and username and password:
    output = run_command_via_ssh(host, username, password, command)
    st.session_state.output = output

# 显示命令输出
st.text_area("命令输出:", st.session_state.output, height=300)

# 提示用户输入命令
if not command:
    st.warning("请输入一个命令。")
if not host or not username or not password:
    st.warning("请输入 SSH 连接信息。")
