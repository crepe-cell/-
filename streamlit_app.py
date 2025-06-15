import streamlit as st
import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error:\n{e.stderr}"

# 检查用户是否已登录
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# 如果用户未登录，显示登录表单
if not st.session_state.logged_in:
    st.title("管理员登录")
    admin_username = st.text_input("请输入管理员账号:")
    admin_password = st.text_input("请输入密码:", type="password")

    if st.button("登录"):
        # 这里设置默认的管理员账号和密码
        if admin_username == "admin" and admin_password == "admin":  # 默认账号和密码
            st.session_state.logged_in = True
            st.success("登录成功！")
        else:
            st.error("登录失败，请检查账号和密码。")
else:
    st.title("Bash 终端模拟")
    
    command = st.text_input("输入 Bash 命令:")
    
    if command.strip():
        output = run_command(command)
        st.text_area("命令输出:", output, height=300)
    else:
        st.warning("请输入命令。")
