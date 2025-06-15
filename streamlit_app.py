import streamlit as st
import geoip2.database
import requests

# GeoIP2 数据库文件路径
DATABASE_PATH = 'MaxMind-DB/test-data/GeoIP2-City-Test.mmdb'  # 替换为你的数据库文件路径

def get_public_ip():
    """获取公共 IP 地址"""
    try:
        response = requests.get('https://api.ipify.org?format=json')
        return response.json()['ip']
    except Exception as e:
        st.error(f"无法获取公共 IP 地址: {e}")
        return None

def get_geolocation(latitude, longitude):
    """根据经纬度获取地理位置信息"""
    reader = geoip2.database.Reader(DATABASE_PATH)
    
    try:
        response = reader.city((latitude, longitude))
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
    st.title("自动地理位置查询")

    # 显示公共 IP 地址
    public_ip = get_public_ip()
    if public_ip:
        st.write(f"检测到的公共 IP 地址: {public_ip}")

    # 显示用户代理信息
    user_agent = st.text_input("用户代理信息", value=requests.utils.default_user_agent(), disabled=True)
    st.write(f"用户代理: {user_agent}")

    # 使用 JavaScript 获取用户的地理位置
    st.markdown("""
    <script>
    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition, showError);
        } else {
            alert("Geolocation is not supported by this browser.");
        }
    }

    function showPosition(position) {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        const data = { latitude: latitude, longitude: longitude };
        fetch('/get_location', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("location").innerHTML = 
                "国家: " + data.country + "<br>" +
                "城市: " + data.city + "<br>" +
                "纬度: " + data.latitude + "<br>" +
                "经度: " + data.longitude + "<br>" +
                "时区: " + data.timezone;
        });
    }

    function showError(error) {
        switch(error.code) {
            case error.PERMISSION_DENIED:
                alert("用户拒绝了请求地理位置的权限。");
                break;
            case error.POSITION_UNAVAILABLE:
                alert("位置信息不可用。");
                break;
            case error.TIMEOUT:
                alert("请求地理位置超时。");
                break;
            case error.UNKNOWN_ERROR:
                alert("发生未知错误。");
                break;
        }
    }
    </script>
    """, unsafe_allow_html=True)

    # 显示位置按钮
    if st.button("获取我的位置"):
        st.markdown("<script>getLocation();</script>", unsafe_allow_html=True)

    # 显示地理位置信息
    st.markdown("<div id='location'></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
