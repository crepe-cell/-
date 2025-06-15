import streamlit as st
import subprocess

def run_script():
    try:
        # 执行 curl 命令并运行下载的脚本
        result = subprocess.run(['curl', '-sSf', 'https://sshx.io/get'], capture_output=True, text=True, check=True)
        # 直接返回脚本的输出
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

# Streamlit 应用
st.title("自动化脚本执行")
st.write("点击下面的按钮执行自动化脚本并显示结果")

if st.button("执行脚本"):
    script_output = run_script()
    st.text(script_output)
