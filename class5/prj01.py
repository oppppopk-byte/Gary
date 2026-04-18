#######################匯入模組#######################
from ttkbootstrap import *
import sys
import os

os.chdir(sys.path[0])
#######################定義函數########################
windows = Tk()
windows.title("My first GUI")
#######################建立視窗########################
################設字形########################
font_size = 20
windows.option_add("*Font", ("Arial", font_size))
##########設定主題##########
style = Style(theme="minty")  # 設定主題
style.configure("my.TButton", font=("Helvetica", font_size))  # 設定按鈕字型

###########建立標籤########################
label1 = Label(windows, text="這是一個標籤")
label1.grid(row=0, column=0, sticky="E")
#################建立按鈕########################
button = Button(windows, text="按我", command=lambda: print("按鈕被按下了"))
button.grid(row=0, column=1, sticky="W")
button2 = Button(windows, text="按我", command=lambda: print("按鈕2被按下了"))
button2.grid(row=1, column=0, columnspan=2, sticky="EW")
# 進入主程式
windows.mainloop()
