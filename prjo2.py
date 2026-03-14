from tkinter import *
from tkinter import *
import random


############定義函數########################
def hi_fun():
    fg_COLORS = "#" + "".join([random.choice("0123456789ABCDEF") for i in range(6)])
    """
    比對展開寫法
    fg_COLORS="#"
    for i in range(6):
        fg_COLORS+=random.choice("0123456789ABCDEF")
    """

    bg_COLORS = "#" + "".join([random.choice("0123456789ABCDEF") for i in range(6)])
    display.config(text="Hi Singular", fg=fg_COLORS, bg=bg_COLORS)


# 清除畫面文字
def clear_fun():
    display.config(text="", fg=windows.cget("bg"), bg=windows.cget("bg"))


# 建立主視窗
windows = Tk()

# 設定視窗標題
windows.title("My first GUI")

# 建立按鈕
btn1 = Button(windows, text="Show Screen", command=hi_fun)
btn1.pack()

# 建立清除按鈕
btn2 = Button(windows, text="Clear", command=clear_fun)
btn2.pack()

# 顯示文字區域
display = Label(windows, text="")
display.pack()

# 進入主程式
windows.mainloop()
