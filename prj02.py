#######################匯入模組#######################
from tkinter import *


#######################定義函數########################
def hi_fun():
    print("Hello, World!")

    display.config(
        text="Hi", fg="red", bg="black"
    )  # 更新標籤的文字、字體顏色和背景顏色


def cl_fun():
    windows.destroy()  # 關閉視窗


#######################建立視窗########################
windows = Tk()  # 建立視窗物件
windows.title("My First Window")  # 設定視窗標題

#######################建立按鈕########################
btn1 = Button(windows, text="show screen", command=hi_fun)
btn1.pack()  # 將按鈕加入視窗並顯示
btn2 = Button(windows, text="Exit", command=cl_fun)
btn2.pack()  # 將按鈕加入視窗並顯示
#######################建立標籤########################
# 創建一個標籤，顯示文字"Hi"，字體顏色為紅色，背景顏色為黑色
# LOBEL參數說明:(視窗名稱，顯示文字，字體顏色，背景顏色)
display = Label(windows, text=" ")
display.pack()  # 將標籤加入視窗並顯示
#######################運行應用程式########################
windows.mainloop()  # 開始執行指迴圈.等待用戶操作
