import subprocess
import sys

# 升级 pip
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])

# 安装 requirements.txt 中的依赖
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
