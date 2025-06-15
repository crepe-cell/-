import subprocess
import sys
import time

def upgrade_pip():
    print("🚀 正在升级 pip...")
    subprocess.run([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)
    print("✅ pip 升级完成！")

def install_requirements():
    print("📦 安装 Streamlit 及必要依赖...")
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'streamlit', 'paramiko'], check=True)
    print("✅ 依赖安装完成！")

def deploy_app():
    print("🚀 启动 Streamlit 终端应用...")
    subprocess.run(["streamlit", "run", "app.py"], check=True)

if __name__ == "__main__":
    upgrade_pip()
    install_requirements()
    time.sleep(2)  # 稍作等待确保安装完成
    deploy_app()
