from tkinter import *

### 建立主視窗 ###
windows = Tk()
# 設定視窗標題
windows.title("My first GUI")
##畫布##
canvas = Canvas(windows, width=600, height=600, bg="white")
canvas.pack()
# 進入主程式
windows.mainloop()
