import streamlit as st
import subprocess

def get_ip_info():
    try:
        # 执行 curl 命令
        result = subprocess.run(['curl', 'ifconfig.me/all'], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

# Streamlit 应用
st.title("IP 信息查询")
st.write("点击下面的按钮获取 IP 信息")

if st.button("获取 IP 信息"):
    ip_info = get_ip_info()
    st.text(ip_info)
