import requests
import os

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "YOUR_API_KEY_HERE")
BASE_URL= "https://api.openweathermap.org/data/2.5/forecast?"
UNITS="metric"
LANG="zh_tw"

city_name = "Taipei"

send_url =(
    f"{BASE_URL}q={city_name}"
    f"&appid={OPENWEATHER_API_KEY}"
    f"&units={UNITS}"
    f"&lang={LANG}"
)
print("發送的URL:", send_url)
response = requests.get(send_url)
response.raise_for_status() 
info = response.json()

if "city" in info:
    for forecast in info["list"]:
        dt_txt = forecast["dt_txt"]
        temp = forecast["main"]["temp"]
        weather_description = forecast["weather"][0]["description"]

        print(dt_txt, temp, weather_description)
else:
    print("無法取得天氣資料，請確認城市名稱是否正確。")

