import streamlit as st
import geoip2.database
import requests

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json')
        return response.json()['ip']
    except Exception as e:
        st.error(f"无法获取公共 IP 地址: {e}")
        return None

def get_geolocation(ip_address):
    # 使用 GeoIP2 测试数据库文件的路径
    database_path = 'MaxMind-DB/test-data/GeoIP2-City-Test.mmdb'  # 替换为你的数据库文件路径
    reader = geoip2.database.Reader(database_path)
    
    try:
        response = reader.city(ip_address)
        return {
            'country': response.country.name,
            'city': response.city.name,
            'latitude': response.location.latitude,
            'longitude': response.location.longitude,
            'timezone': response.location.time_zone
        }
    except Exception as e:
        st.error(f"无法获取地理位置信息: {e}")
        return None
    finally:
        reader.close()

def main():
    st.title("自动 IP 地理位置查询")
    
    # 获取用户的公共 IP 地址
    ip_address = get_public_ip()
    if ip_address:
        st.write(f"检测到的公共 IP 地址: {ip_address}")
        
        # 查询地理位置信息
        data = get_geolocation(ip_address)
        if data:
            st.subheader("地理位置信息")
            st.write(f"国家: {data['country']}")
            st.write(f"城市: {data['city']}")
            st.write(f"纬度: {data['latitude']}")
            st.write(f"经度: {data['longitude']}")
            st.write(f"时区: {data['timezone']}")
        else:
            st.error("未找到该 IP 地址的信息。")
    else:
        st.warning("无法检测到公共 IP 地址。")

if __name__ == "__main__":
    main()
