#######匯入模組#######
from tkinter import *
import sys
import os

#######設定工作目錄#######
os.chdir(sys.path[0])
### 建立主視窗 ###
windows = Tk()
# 設定視窗標題
windows.title("My first GUI")
##畫布##
canvas = Canvas(windows, width=600, height=600, bg="#C73838")
canvas.pack()
# 進入主程式
windows.mainloop()
