import streamlit as st
import subprocess

# 用于存储用户名的 Session State
if "username" not in st.session_state:
    st.session_state.username = None

# 弹窗输入用户名（首次进入）
if st.session_state.username is None:
    with st.modal("请输入用户名", True):
        username_input = st.text_input("用户名:", key="username_input")
        if st.button("确认"):
            if username_input.strip():
                st.session_state.username = username_input.strip()
                st.experimental_rerun()
            else:
                st.warning("用户名不能为空")

# 只有输入了用户名才显示主界面
if st.session_state.username:
    # 页面布局，居中顶部显示标题和按钮
    st.markdown(
        """
        <style>
        .main > div:first-child {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            margin-top: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title(f"欢迎，{st.session_state.username}！Web 终端模拟")

    # ChatUI 按钮
    if st.button("ChatUI"):
        # 简单聊天界面示例
        st.write("开始与伙伴聊天...")
        chat_input = st.text_input("输入消息并回车发送", key="chat_input")
        if chat_input:
            st.write(f"你说: {chat_input}")
            # 这里可以接入聊天机器人或伙伴聊天逻辑

    else:
        # 命令行输入框，支持回车执行
        command = st.text_input("输入命令并按 Enter 执行:", key="command_input")

        if command:
            # 回车后自动执行命令
            def run_command(command):
                try:
                    result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
                    return result.stdout
                except subprocess.CalledProcessError as e:
                    return f"Error: {e}"

            output = run_command(command)
            st.text_area("命令输出:", output, height=300)
