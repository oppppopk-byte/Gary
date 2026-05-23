# Weather App（可切換溫度單位版）

import tkinter as tk
from tkinter import messagebox

# 主視窗
window = tk.Tk()
window.title("Weather App")
window.geometry("720x400")
window.configure(bg="#1e1f26")

# 外框
weather_box = tk.Frame(
    window,
    bg="#f5f5f5",
    width=680,
    height=340
)
weather_box.place(x=20, y=20)

# 標題
title_label = tk.Label(
    weather_box,
    text="城市：",
    font=("Microsoft JhengHei", 20, "bold"),
    fg="#666",
    bg="#f5f5f5"
)
title_label.place(x=20, y=30)

# 輸入框
city_entry = tk.Entry(
    weather_box,
    font=("Microsoft JhengHei", 18),
    width=25
)
city_entry.place(x=120, y=30)

# 溫度單位變數
unit_var = tk.StringVar(value="C")

# 攝氏按鈕
c_button = tk.Radiobutton(
    weather_box,
    text="°C",
    variable=unit_var,
    value="C",
    font=("Microsoft JhengHei", 16),
    bg="#f5f5f5"
)
c_button.place(x=120, y=90)

# 華氏按鈕
f_button = tk.Radiobutton(
    weather_box,
    text="°F",
    variable=unit_var,
    value="F",
    font=("Microsoft JhengHei", 16),
    bg="#f5f5f5"
)
f_button.place(x=200, y=90)

# 顯示天氣資訊
def show_weather():

    city = city_entry.get()

    if city == "":
        messagebox.showwarning("提醒", "請輸入城市名稱")
        return

    # 假設原本溫度是 28°C
    celsius = 28

    # 判斷單位
    if unit_var.get() == "C":
        temp = f"{celsius}°C"
    else:
        fahrenheit = (celsius * 9 / 5) + 32
        temp = f"{fahrenheit:.1f}°F"

    # 顯示資料
    weather_result.config(
        text=f"""
城市：{city}

天氣：晴天 ☀️
溫度：{temp}
濕度：65%
風速：3 m/s
"""
    )

# 查詢按鈕
search_button = tk.Button(
    weather_box,
    text="查詢",
    font=("Microsoft JhengHei", 18),
    bg="#a8e6cf",
    fg="white",
    activebackground="#90d8bb",
    relief="flat",
    command=show_weather
)
search_button.place(x=520, y=25)

# 天氣資訊區
weather_result = tk.Label(
    weather_box,
    text="請輸入城市後查詢",
    font=("Microsoft JhengHei", 18),
    bg="#f5f5f5",
    justify="left"
)
weather_result.place(x=180, y=170)

# 執行程式
window.mainloop()