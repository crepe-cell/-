import streamlit as st
import subprocess
import paramiko
import platform
import sys

# **pip 升级**
def upgrade_pip():
    try:
        result = subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], capture_output=True, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return f"❌ pip 升级失败: {e}"

# **网络检测函数**
def check_network():
    try:
        ping_cmd = ["ping", "-c", "1", "8.8.8.8"] if platform.system() != "Windows" else ["ping", "-n", "1", "8.8.8.8"]
        result = subprocess.run(ping_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return "🟢 网络连接正常" if result.returncode == 0 else "🔴 网络异常"
    except Exception as e:
        return f"⚠️ 错误: {e}"

# **页面设置**
st.set_page_config(layout="wide", page_title="SSH 终端 - Tabby 模拟")
st.markdown("""
<style>
    body { background-color: #1E1E1E; color: white; }
    .stButton > button { background-color: #FF5733; color: white; border-radius: 5px; }
    .stExpander { background-color: #252526; }
</style>
""", unsafe_allow_html=True)

st.title("🚀 SSH 终端 - 模拟 Tabby & sshx.io")

# **pip 升级按钮**
if st.sidebar.button("⚡ 升级 pip"):
    result = upgrade_pip()
    st.sidebar.text_area("pip 升级结果:", result, height=150)

# **侧边栏 - 网络状态显示**
status = check_network()
st.sidebar.success(status) if "网络连接正常" in status else st.sidebar.error(status)

# **终端管理**
if "terminals" not in st.session_state:
    st.session_state.terminals = []
if "terminal_history" not in st.session_state:
    st.session_state.terminal_history = {}

# **添加终端**
if st.sidebar.button("➕ 创建终端"):
    terminal_id = len(st.session_state.terminals) + 1
    st.session_state.terminals.append(terminal_id)
    st.session_state.terminal_history[terminal_id] = []

# **显示所有终端**
for i, terminal_id in enumerate(st.session_state.terminals):
    with st.expander(f"🖥️ 终端 {terminal_id}"):
        command = st.text_input(f"🔹 输入命令 (终端 {terminal_id}):", key=f"cmd_{terminal_id}")

        if st.button(f"✅ 执行 (终端 {terminal_id})", key=f"exec_{terminal_id}"):
            try:
                output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                result = output.stdout.strip()

                # **保存历史**
                st.session_state.terminal_history[terminal_id].append(f"$ {command}\n{result}")

                # **显示命令历史**
                st.text_area(f"📜 命令历史 (终端 {terminal_id}):", "\n".join(st.session_state.terminal_history[terminal_id]), height=200)
            except Exception as e:
                st.error(f"⚠️ 命令执行失败: {e}")

        # **SSH 连接**
        ssh_host = st.text_input(f"🌍 SSH 服务器地址 (终端 {terminal_id}):", key=f"ssh_host_{terminal_id}")
        ssh_user = st.text_input(f"👤 用户名 (终端 {terminal_id}):", key=f"ssh_user_{terminal_id}")
        ssh_pass = st.text_input(f"🔑 密码 (终端 {terminal_id}):", key=f"ssh_pass_{terminal_id}", type="password")

        if st.button(f"🔗 连接 SSH (终端 {terminal_id})", key=f"ssh_connect_{terminal_id}"):
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ssh_host, username=ssh_user, password=ssh_pass, timeout=5)
                st.success(f"✅ 成功连接到 {ssh_host}")
                ssh.close()
            except Exception as e:
                st.error(f"❌ SSH 连接失败: {e}")

        # **关闭终端**
        if st.button(f"❌ 关闭终端 {terminal_id}", key=f"close_{terminal_id}"):
            del st.session_state.terminal_history[terminal_id]
            st.session_state.terminals.pop(i)
            st.experimental_rerun()
