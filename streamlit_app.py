import streamlit as st
import subprocess
import os

# 设置标题
st.title("Docker Pull KasmVNC Image")

# 提示用户输入镜像
st.write("点击下面的按钮来拉取 KasmVNC 的 AlmaLinux 8 桌面镜像。")

# 运行 Docker 命令的函数
def pull_docker_image():
    try:
        # 执行 Docker 拉取命令
        result = subprocess.run(["docker", "pull", "kasmweb/almalinux-8-desktop"], 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        # 返回命令输出
        return result.stdout
    except subprocess.CalledProcessError as e:
        # 如果出错，返回错误信息
        return f"Error: {e.stderr}"

# 在 Streamlit 上创建一个按钮，点击后执行 Docker 拉取
if st.button('Pull AlmaLinux 8 Desktop Docker Image'):
    st.write("正在拉取镜像，请稍等...")

    # 执行 Docker 命令并显示结果
    output = pull_docker_image()

    # 显示拉取结果或错误信息
    st.text_area("Docker Pull Output", output, height=300)

