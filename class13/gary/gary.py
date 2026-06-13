#######################匯入模組#######################
import requests #匯入requests模組，這是一個用於發送HTTP請求的庫

#######################定義類別#######################
class WeatherAPI:
    """把OpenWeather的查詢流程整理成可重複使用的工具類別."""
    def __init__(self, api_key, lang='zh_tw'):
        self.api_key = api_key
        self.units = 'metric'
        self.lang = lang
        self.base_url = 'https://api.openweathermap.org/data/2.5/weather?'
        self.forecast_url = 'https://api.openweathermap.org/data/2.5/forecast?'
        self.icon_url = 'https://openweathermap.org/img/wn  /'
    def get_current_weather(self, city_name):
        send_url=(
            f"{self.base_url}appid={self.api_key}&q={city_name}"
            f"&units={self.units}&lang={self.lang}"
        )
        response = requests.get(send_url)
        return response.json()
    def get_weather_summary(self, city_name):
        info = self.get_current_weather(city_name)

        if "weather" in info and "main" in info:
            return {
                "city_name":info.get("name", city_name),
                "temperature_celsius":round(info["main"]["temp"], 2),
                "description":info["weather"][0]["description"],
                "icon_code":info["weather"][0]["icon"],
            }
        return None
    def get_icon_url(self, icon_code): 
        return f"{self.icon_url}{icon_code}@2x.png"
    def get_icon(self, icon_code):
        icon_url = self.get_icon_url(icon_code)
        response = requests.get(icon_url)
        if response.status_code == 200:
            return response.content
        return None   
    def get_forecast(self, city_name):
        send_url =(
            f"{self.forecast_url}q={city_name}&appid={self.api_key}"
            f"&units={self.units}&lang={self.lang}"
        )
        response = requests.get(send_url)
        response.raise_for_status()
        return response.json()
    def get_forecast_summary(self, city_name, count=10):
        forecast_count = max(0, count)
        try:
            info = self.get_forecast(city_name)
        except requests.HTTPError as error:
              response = error.response
              if response is not None and response.status_code == 404:
                  return None
              raise
        if "city" not in info or "list" not in info:
            return None

        city_label=info["city"].get("name", city_name)
        forecast_summary = []

        for forecast in info["list"][:forecast_count]:
            forecast_summary.append(
                {
                "city_name": city_label,
                "datetime": forecast["dt_txt"],
                "temperature_celsius": round(forecast["main"]["temp"], 2),
                "description": forecast["weather"][0]["description"],
                "icon_code": forecast["weather"][0]["icon"],
                }
            )

        return forecast_summary