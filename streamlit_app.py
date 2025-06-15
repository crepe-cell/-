import streamlit as st
import subprocess

# 会话状态存储用户名和聊天窗口显示状态及聊天记录
if "username" not in st.session_state:
    st.session_state.username = ""
if "show_chat" not in st.session_state:
    st.session_state.show_chat = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 用户名输入逻辑（简易版）
if not st.session_state.username:
    st.write("请输入用户名：")
    username_input = st.text_input("用户名")
    if st.button("确认"):
        if username_input.strip():
            st.session_state.username = username_input.strip()
            st.experimental_rerun()
        else:
            st.warning("用户名不能为空")
else:
    st.title(f"欢迎，{st.session_state.username}！Web 终端模拟")

# 聊天按钮，使用聊天气泡图标（Material icon: :material/chat:）
if st.button("聊天", icon=":material/chat:"):
    st.session_state.show_chat = not st.session_state.show_chat

# 聊天窗口左下角固定样式
st.markdown(
    """
    <style>
    .chat-box {
        position: fixed;
        bottom: 60px;  /* 留出输入框空间 */
        left: 20px;
        width: 300px;
        height: 340px;
        background-color: #f0f2f6;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 10px;
        overflow-y: auto;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        z-index: 9999;
        font-size: 14px;
    }
    .chat-input {
        position: fixed;
        bottom: 20px;
        left: 20px;
        width: 300px;
        z-index: 10000;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 显示聊天窗口和输入框
if st.session_state.show_chat:
    st.markdown('<div class="chat-box">', unsafe_allow_html=True)
    st.write("💬 伙伴聊天开始了！")
    # 显示聊天记录
    for msg in st.session_state.chat_history:
        st.write(msg)
    st.markdown('</div>', unsafe_allow_html=True)

    # 聊天输入框固定在左下角，回车发送
    chat_input = st.text_input("", key="chat_input", placeholder="输入消息并回车发送", label_visibility="collapsed")
    if chat_input:
        st.session_state.chat_history.append(f"你说: {chat_input}")
        # 清空输入框
        st.session_state.chat_input = ""
        st.experimental_rerun()

# 命令行输入框
if not st.session_state.show_chat:
    command = st.text_input("输入命令并按 Enter 执行:", key="command_input")
    if command:
        def run_command(command):
            try:
                result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
                return result.stdout
            except subprocess.CalledProcessError as e:
                return f"Error: {e}"
        output = run_command(command)
        st.text_area("命令输出:", output, height=300)
