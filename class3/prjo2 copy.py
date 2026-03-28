from tkinter import *
import sys
import os
from PIL import Image, ImageTk

########設定工作目錄#######3
os.chdir(sys.path[0])
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
# 進入主程式
windows.mainloop()
