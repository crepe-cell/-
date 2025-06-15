import streamlit as st
import subprocess

st.title("📡 远程终端共享 - Tmate")

# 启动 tmate 并获取共享链接
if st.button("启动 tmate"):
    with st.spinner("正在启动 tmate..."):
        process = subprocess.Popen(["tmate", "-F"], stdout=subprocess.PIPE, text=True)
        output, _ = process.communicate()
    
    if output:
        st.success("✅ Tmate 会话已启动！")
        st.text_area("🔗 共享链接", output, height=150)
    else:
        st.error("❌ 启动 tmate 失败，请检查安装！")
