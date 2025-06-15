import streamlit as st
import subprocess

# 设置页面标题
st.title("仿真Web终端")

# 创建标签页
tabs = st.tabs(["终端1", "终端2", "终端3"])

# 在每个标签页中实现终端功能
for tab in tabs:
    with tab:
        st.subheader(f"{tab} - 输入命令")
        
        # 创建一个文本输入框用于输入命令
        command = st.text_input("输入命令:", "")
        
        if st.button("执行"):
            if command:
                try:
                    # 使用subprocess模块执行命令并返回结果
                    result = subprocess.run(command, shell=True, capture_output=True, text=True)
                    output = result.stdout if result.stdout else result.stderr
                except Exception as e:
                    output = str(e)
                
                # 显示输出
                st.text_area("输出:", output, height=200)
            else:
                st.warning("请输入命令！")

# 运行应用
if __name__ == "__main__":
    st.run()
