import streamlit as st
import subprocess

# 设置 Streamlit 页面标题
st.title("Docker Command Executor")

# 创建一个按钮来执行 Docker 命令
if st.button("Run Docker Command"):
    # 定义 Docker 命令
    command = [
        "docker", "run", "-it", "--rm", "--name", "windows",
        "-p", "8006:8006", "--device=/dev/kvm", "--device=/dev/net/tun",
        "--cap-add", "NET_ADMIN", "-v", f"{PWD:-.}/windows:/storage",
        "--stop-timeout", "120", "dockurr/windows"
    ]
    
    try:
        # 执行 Docker 命令
        result = subprocess.run(command, capture_output=True, text=True)
        
        # 显示命令输出
        st.text("Command Output:")
        st.text(result.stdout)
        
        # 显示错误信息（如果有）
        if result.stderr:
            st.text("Error:")
            st.text(result.stderr)
    except Exception as e:
        st.text(f"An error occurred: {e}")
