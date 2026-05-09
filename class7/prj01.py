# 匯入 ttkbootstrap（美化 tkinter 介面）
from ttkbootstrap import *

# 匯入圖片處理模組
from PIL import Image, ImageTk

# 匯入 requests（抓取 API 資料）
import requests

# 可以把網路圖片轉成記憶體資料
from io import BytesIO


# =========================
# OpenWeather API 設定
# =========================

# API 金鑰
API_KEY = "你的API_KEY"

# API 網址
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# 溫度單位（metric = 攝氏）
UNITS = "metric"

# 語言（繁體中文）
LANGU = "zh_tw"

# 天氣圖標網址
ICON_BASE_URL = "https://openweathermap.org/img/wn/"


# =========================
# 目前溫度（攝氏）
# =========================
current_temp_c = 0


# =========================
# 查詢天氣
# =========================
def get_weather():

    # 使用全域變數
    global current_temp_c

    # 取得輸入框內容
    city = city_entry.get()

    # 如果沒輸入城市
    if city == "":
        temp_label.config(text="請輸入城市")
        return

    # API網址
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=zh_tw"

    # 取得JSON資料
    data = requests.get(url).json()

    # 如果成功找到城市
    if data["cod"] == 200:

        # 取得攝氏溫度
        current_temp_c = data["main"]["temp"]

        # 取得天氣描述
        desc = data["weather"][0]["description"]

        # 取得圖標代碼
        icon_code = data["weather"][0]["icon"]

        # 組合圖標網址
        icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"

        # 下載圖片
        response = requests.get(icon_url)

        # 將圖片資料轉成圖片格式
        image_data = Image.open(BytesIO(response.content))

        # 轉成 tkinter 可以使用的圖片格式
        photo = ImageTk.PhotoImage(image_data)

        # 顯示圖片
        icon_label.config(image=photo)

        # 防止圖片被清除
        icon_label.image = photo

        # 更新溫度
        update_temperature()

        # 顯示描述
        desc_label.config(text=f"描述: {desc}")

    # 如果找不到城市
    else:

        temp_label.config(text="找不到城市")

        desc_label.config(text="")

        icon_label.config(image="")


# =========================
# 更新溫度
# =========================
def update_temperature():

    # 如果勾選 -> 顯示華氏
    if temp_var.get():

        # 攝氏轉華氏公式
        f = (current_temp_c * 9 / 5) + 32

        temp_label.config(text=f"溫度: {f:.1f}°F")

    # 沒勾選 -> 顯示攝氏
    else:

        temp_label.config(text=f"溫度: {current_temp_c:.1f}°C")


# =========================
# 建立視窗
# =========================

# 建立主視窗
window = Window(themename="minty")

# 視窗標題
window.title("Weather App")

# 讓中間欄位可以自動伸縮
window.columnconfigure(1, weight=1)


# =========================
# 樣式設定
# =========================

# 取得 style
style = window.style

# Label 樣式
style.configure(
    "Weather.TLabel",
    font=("微軟正黑體", 24)
)

# Entry 樣式
style.configure(
    "Weather.TEntry",
    font=("微軟正黑體", 24)
)

# Button 樣式
style.configure(
    "Weather.TButton",
    font=("微軟正黑體", 22)
)

# Checkbutton 樣式
style.configure(
    "Weather.TCheckbutton",
    font=("微軟正黑體", 18)
)


# =========================
# 城市文字
# =========================
city_label = Label(
    window,
    text="請輸入想搜尋的城市：",
    style="Weather.TLabel",
)

city_label.grid(
    row=0,
    column=0,
    padx=(20, 10),
    pady=(20, 10),
    sticky="w"
)


# =========================
# 輸入框
# =========================
city_entry = Entry(
    window,
    width=20,
    style="Weather.TEntry"
)

city_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=(20, 10),
    sticky="ew"
)


# =========================
# 查詢按鈕
# =========================
search_button = Button(
    window,
    text="獲得天氣資訊",
    style="Weather.TButton",
    command=get_weather,
)

search_button.grid(
    row=0,
    column=2,
    padx=(10, 20),
    pady=(20, 10)
)


# =========================
# 天氣圖片
# =========================
icon_label = Label(window)

icon_label.grid(
    row=1,
    column=0,
    padx=20,
    pady=20
)


# =========================
# 溫度顯示
# =========================
temp_label = Label(
    window,
    text="溫度: ?°C",
    style="Weather.TLabel",
)

temp_label.grid(
    row=1,
    column=1,
    padx=20,
    pady=20
)


# =========================
# 天氣描述
# =========================
desc_label = Label(
    window,
    text="描述: ?",
    style="Weather.TLabel"
)

desc_label.grid(
    row=1,
    column=2,
    padx=20,
    pady=20
)


# =========================
# 勾選變數
# =========================
temp_var = BooleanVar()


# =========================
# 勾選框
# =========================
check = Checkbutton(
    window,
    text="切換成華氏溫度 °F",
    variable=temp_var,
    style="Weather.TCheckbutton",
    command=update_temperature,
)

check.grid(
    row=2,
    column=0,
    columnspan=3,
    pady=(0, 20)
)


# =========================
# 啟動程式
# =========================
window.mainloop()