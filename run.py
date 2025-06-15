import streamlit as st
import subprocess

def run_command():
    try:
        # 执行命令
        result = subprocess.run(
            ["curl", "-sSf", "https://sshx.io/get"],
            capture_output=True,
            text=True,
            check=True
        )
        # 将结果传递给 sh
        subprocess.run(["sh", "-s", "run"], input=result.stdout, text=True, check=True)
        st.success("命令执行成功！")
    except subprocess.CalledProcessError as e:
        st.error(f"命令执行失败: {e}")

st.title("执行 Shell 命令")
if st.button("运行命令"):
    run_command()
