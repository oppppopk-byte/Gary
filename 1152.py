# Weather App（含天氣圖片顯示版）

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# =========================
# 主視窗
# =========================
window = tk.Tk()
window.title("Weather App")
window.geometry("720x420")
window.configure(bg="#1e1f26")

# =========================
# 白色外框
# =========================
weather_box = tk.Frame(
    window,
    bg="#f5f5f5",
    width=700,
    height=380
)
weather_box.place(x=10, y=20)

# =========================
# 標題
# =========================
title_label = tk.Label(
    weather_box,
    text="請輸入想搜尋的城市:",
    font=("Microsoft JhengHei", 20, "bold"),
    fg="#666",
    bg="#f5f5f5"
)
title_label.place(x=10, y=25)

# =========================
# 輸入框
# =========================
city_entry = tk.Entry(
    weather_box,
    font=("Microsoft JhengHei", 18),
    width=20
)
city_entry.place(x=240, y=28)

# =========================
# 溫度顯示
# =========================
temp_label = tk.Label(
    weather_box,
    text="溫度: ?°C",
    font=("Microsoft JhengHei", 20, "bold"),
    fg="#666",
    bg="#f5f5f5"
)
temp_label.place(x=320, y=90)

# =========================
# 描述顯示
# =========================
desc_label = tk.Label(
    weather_box,
    text="描述: ?",
    font=("Microsoft JhengHei", 20, "bold"),
    fg="#666",
    bg="#f5f5f5"
)
desc_label.place(x=560, y=90)

# =========================
# 天氣圖片區
# =========================
image_label = tk.Label(
    weather_box,
    text="天氣圖標",
    font=("Microsoft JhengHei", 22, "bold"),
    bg="#f5f5f5"
)
image_label.place(x=80, y=90)

# =========================
# 溫度單位
# =========================
unit_var = tk.StringVar(value="C")

unit_check = tk.Checkbutton(
    weather_box,
    text="溫度單位(°C/°F)",
    variable=unit_var,
    onvalue="F",
    offvalue="C",
    font=("Microsoft JhengHei", 18),
    bg="#f5f5f5",
    fg="#666"
)
unit_check.place(x=240, y=140)

# =========================
# 建立圖片
# =========================
# 你可以換成自己的圖片檔案
# sunny.png / rainy.png

# 預設圖片
weather_image = Image.open("sunny.png")
weather_image = weather_image.resize((120, 120))

weather_photo = ImageTk.PhotoImage(weather_image)

image_label.config(image=weather_photo)
image_label.image = weather_photo

# =========================
# 查詢天氣
# =========================
def get_weather():

    city = city_entry.get()

    if city == "":
        messagebox.showwarning("提醒", "請輸入城市")
        return

    # 假資料
    weather = "晴天"
    celsius = 28

    # 單位轉換
    if unit_var.get() == "C":
        temp_text = f"溫度: {celsius}°C"
    else:
        fahrenheit = (celsius * 9 / 5) + 32
        temp_text = f"溫度: {fahrenheit:.1f}°F"

    # 更新文字
    temp_label.config(text=temp_text)
    desc_label.config(text=f"描述: {weather}")

    # 更新圖片
    if weather == "晴天":
        img = Image.open("sunny.png")

    elif weather == "下雨":
        img = Image.open("rainy.png")

    else:
        img = Image.open("cloudy.png")

    img = img.resize((120, 120))

    photo = ImageTk.PhotoImage(img)

    image_label.config(image=photo)
    image_label.image = photo

# =========================
# 查詢按鈕
# =========================
search_button = tk.Button(
    weather_box,
    text="獲得天氣資訊",
    font=("Microsoft JhengHei", 18, "bold"),
    bg="#a8e6cf",
    fg="white",
    activebackground="#90d8bb",
    relief="flat",
    command=get_weather
)
search_button.place(x=520, y=25)

# =========================
# 執行
# =========================
window.mainloop()