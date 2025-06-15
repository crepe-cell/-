import geoip2.database
import streamlit as st

def get_geolocation(ip_address):
    # 使用 GeoLite2 数据库文件的路径
    database_path = 'GeoLite2-City.mmdb'  # 替换为你的数据库文件路径
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
    st.title("IP 地理位置查询")
    
    ip_address = st.text_input("请输入 IP 地址:", "8.8.8.8")
    
    if st.button("查询"):
        if ip_address:
            data = get_geolocation(ip_address)
            if data:
                st.subheader("地理位置信息")
                st.write(f"国家: {data['country']}")
                st.write(f"城市: {data['city']}")
                st.write(f"纬度: {data['latitude']}")
                st.write(f"经度: {data['longitude']}")
                st.write(f"时区: {data['timezone']}")
        else:
            st.warning("请输入有效的 IP 地址。")

if __name__ == "__main__":
    main()
