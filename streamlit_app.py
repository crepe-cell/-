import streamlit as st
import nmap

# 端口用途字典
PORT_INFO = {
    "80": "HTTP，网页服务器默认端口",
    "443": "HTTPS，安全加密网页服务端口",
    "5080": "VoIP或流媒体服务常用端口",
    "21": "FTP控制端口，用于文件传输控制",
    "22": "SSH，安全远程登录端口",
    "23": "Telnet，远程登录端口（明文传输，安全性低）",
    "3306": "MySQL数据库服务端口",
    "3389": "RDP，Windows远程桌面端口",
    "8808": "自定义或管理接口端口，具体视应用而定",
    "8006": "Proxmox VE虚拟化管理界面端口",
    "8008": "HTTP备用端口，常见于Web或代理服务"
}

DEFAULT_PORTS = ",".join(PORT_INFO.keys())

# Streamlit页面配置
st.set_page_config(page_title="Nmap端口扫描器", layout="centered")

# 自定义CSS样式
st.markdown("""
<style>
body {
    background-color: #f0f2f6;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
h1 {
    color: #4B8BBE;
    text-align: center;
}
.stButton>button {
    background-color: #4B8BBE;
    color: white;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px 20px;
}
.stButton>button:hover {
    background-color: #306998;
    color: #fff;
}
.port-table {
    border-collapse: collapse;
    width: 100%;
}
.port-table th, .port-table td {
    border: 1px solid #ddd;
    padding: 8px;
}
.port-table th {
    background-color: #4B8BBE;
    color: white;
    text-align: left;
}
.open-port {
    color: green;
    font-weight: bold;
}
.closed-port {
    color: red;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# 标题
st.title("Nmap端口扫描器")

# 输入目标IP或域名
target = st.text_input("请输入目标IP或域名", value="127.0.0.1")

# 输入端口，自定义端口，默认填充
ports_input = st.text_input("请输入端口列表（逗号分隔）", value=DEFAULT_PORTS)

# 扫描按钮
if st.button("开始扫描"):
    if not target.strip():
        st.error("目标IP或域名不能为空！")
    else:
        scanner = nmap.PortScanner()
        try:
            # 调用nmap扫描，带服务版本检测
            scan_result = scanner.scan(target, ports_input, arguments='-sS -sV')
            # 解析结果
            if target not in scan_result['scan']:
                st.warning("目标无响应或无法扫描。")
            else:
                st.subheader(f"扫描结果 - {target}")
                ports_data = scan_result['scan'][target].get('tcp', {})
                if not ports_data:
                    st.info("未检测到开放端口。")
                else:
                    # 构建结果表格
                    rows = []
                    for port, info in sorted(ports_data.items()):
                        state = info['state']
                        service = info.get('name', '')
                        version = info.get('version', '')
                        usage = PORT_INFO.get(str(port), "未知端口")
                        state_class = "open-port" if state == "open" else "closed-port"
                        rows.append(f"""
                        <tr>
                            <td>{port}</td>
                            <td>{state}</td>
                            <td>{service} {version}</td>
                            <td>{usage}</td>
                        </tr>
                        """)
                    table_html = f"""
                    <table class="port-table">
                        <thead>
                            <tr>
                                <th>端口</th>
                                <th>状态</th>
                                <th>服务及版本</th>
                                <th>端口用途说明</th>
                            </tr>
                        </thead>
                        <tbody>
                            {''.join(rows)}
                        </tbody>
                    </table>
                    """
                    st.markdown(table_html, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"扫描异常：{e}")
