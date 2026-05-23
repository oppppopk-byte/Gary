
import tkinter as tk
from tkinter import messagebox

# 建立主視窗
window = tk.Tk()
window.title("Weather App")
window.geometry("720x350")
window.configure(bg="#1e1f26")

# 外框
weather_box = tk.Frame(
    window,
    bg="#f5f5f5",
    width=680,
    height=300,
    bd=0
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

# 顯示天氣資訊的函式
def show_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showwarning("提醒", "請輸入城市名稱")
        return

    # 模擬天氣資料
    weather_result.config(
        text=f"""
城市：{city}

天氣：晴天 ☀️
溫度：28°C
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
weather_result.place(x=200, y=120)

# 執行程式
window.mainloop()
 