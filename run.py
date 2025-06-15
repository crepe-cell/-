import subprocess

expected_sha256 = "f9ec2bcb6da70304c49ff331b965dde82e313b4aa354322000e42b0540e48c72"
file_path = "run.py"

# 计算文件 SHA-256
file_hash = calculate_sha256(file_path)

# 校验哈希值并执行 Python 文件
if file_hash == expected_sha256:
    print("哈希匹配，执行文件...")
    subprocess.run(["python3", file_path])
else:
    print("哈希不匹配，禁止执行！")
