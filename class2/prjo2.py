from tkinter import *


############定義函數########################
def hi_fun():
    global change
    if change == False:
        display.config(text="", fg="white", bg="white")
    else:
        display.config(text="Hi Singular", fg="red", bg="black")
    change = not (change)


change = False


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
