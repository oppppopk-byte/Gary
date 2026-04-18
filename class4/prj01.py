from tkinter import *
import sys
import os
from PIL import Image, ImageTk

########設定工作目錄#######3
os.chdir(sys.path[0])


# event.keysym 可以告訴我們使用著剛剛按什麼按鈕
def move_circle(event):
    # 取得按下的按鍵
    key = event.keysym
    # 印出按鍵名稱
    print(key)
    # 根據按下的按鍵來移動圓形
    if key == "Up":
        canvas.move(circle, 0, -10)
    elif key == "Down":
        canvas.move(circle, 0, 10)
    elif key == "Left":
        canvas.move(circle, -10, 0)
    elif key == "Right":
        canvas.move(circle, 10, 0)
    elif key == "d":
        canvas.move(rect, 10, 0)
    elif key == "a":
        canvas.move(rect, -10, 0)
    elif key == "w":
        canvas.move(rect, 0, -10)
    elif key == "s":
        canvas.move(rect, 0, 10)


### 建立主視窗 ###
windows = Tk()
# 設定視窗標題
windows.title("My first GUI")
##畫布##
canvas = Canvas(windows, width=600, height=600, bg="white")
canvas.pack()
######設定視窗圖片######
# 設定視窗圖片
windows.iconbitmap("1.png")
# 仔入圖片
# img = PhotoImage(file="1.png")
image = Image.open("1.png")
img = ImageTk.PhotoImage(image)
# tkinter內建photoimage只能讀取png.GIF.pgm.ppm格式的圖片(不支援jpg.bpm等格式)
######在畫布上顯示圖片##
my_ing = canvas.create_image(300, 300, image=img)
#######################畫圖形########################
# Canvas 畫圖指令的座標都是以畫布左上角為基準
# 在畫布上畫一個圓形，起始位置為 (250,150)，結束位置為 (300,200)，填充顏色為紅色
circle = canvas.create_oval(250, 150, 300, 200, fill="#73E8FF")

# 在畫布上畫一個矩形，起始位置為 (220,400)，結束位置為 (340,430)，填充顏色為藍色
rect = canvas.create_rectangle(220, 400, 340, 430, fill="blue")

# 在畫布上顯示一段文字，位置為 (300,100)，文字為 Corcodile，顏色為黑色，字型為 Arial，大小為 30
msg = canvas.create_text(300, 100, text="Corcodile", fill="black", font=("Arial", 30))
#######################綁定按鍵事件########################
# bind_all("<Key>", ...) 會讓視窗收到鍵盤輸入時呼叫 move_circle
canvas.bind_all("<Key>", move_circle)
# 進入主程式
windows.mainloop()
