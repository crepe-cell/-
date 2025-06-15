import streamlit as st
import subprocess

# **网络检测**
def check_network():
    try:
        result = subprocess.run(["ping", "-c", "1", "8.8.8.8"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return "网络连接正常" if result.returncode == 0 else "网络异常"
    except Exception as e:
        return f"错误: {e}"

st.set_page_config(layout="wide")
st.title("网络终端 - 多终端支持")

# **侧边栏 - 显示网络状态**
status = check_network()
st.sidebar.success(status) if status == "网络连接正常" else st.sidebar.error(status)

# **终端管理**
if "terminals" not in st.session_state:
    st.session_state.terminals = []
if "terminal_history" not in st.session_state:
    st.session_state.terminal_history = {}

# **添加终端**
if st.button("➕ 创建终端"):
    terminal_id = len(st.session_state.terminals) + 1
    st.session_state.terminals.append(terminal_id)
    st.session_state.terminal_history[terminal_id] = []

# **显示终端**
for i, terminal_id in enumerate(st.session_state.terminals):
    with st.expander(f"终端 {terminal_id}"):
        command = st.text_input(f"输入命令 (终端 {terminal_id}):", key=f"cmd_{terminal_id}")

        if st.button(f"执行 (终端 {terminal_id})", key=f"exec_{terminal_id}"):
            try:
                output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                result = output.stdout

                # **保存历史**
                st.session_state.terminal_history[terminal_id].append(f"$ {command}\n{result}")

                # **显示所有历史**
                st.text_area(f"命令输出 (终端 {terminal_id}):", "\n".join(st.session_state.terminal_history[terminal_id]), height=200)
            except Exception as e:
                st.error(f"命令执行失败: {e}")

        # **关闭终端**
        if st.button(f"❌ 关闭终端 {terminal_id}", key=f"close_{terminal_id}"):
            del st.session_state.terminal_history[terminal_id]
            st.session_state.terminals.pop(i)
            st.experimental_rerun()
