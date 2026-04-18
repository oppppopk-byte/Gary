#######################匯入模組#######################
from ttkbootstrap import *
import sys
import os
from tkinter import filedialog
from PIL import Image, ImageTk

#######################定義函數########################
windows = Tk()
windows.title("My first GUI")
###########建立標籤########################
label1 = Label(windows, text="這是一個標籤")
label1.grid(row=0, column=0, sticky="E")
label2 = Label(windows, text="這是第二個標籤")
label2.grid(row=0, column=1, sticky="E")


####定義函數###
def open_file():
    global file_path
    file_path = filedialog.askopenfilename(initialdir=sys.path[0])
    label2.config(text=file_path)
    Canvas = Canvas(windows, width=600, height=600)
    Canvas.grid(row=3, column=0, columnspan=3)


def show_image():  # 顯示圖片
    global file_path

    image = Image.open(file_path)  # 打開圖片檔案

    # 調整圖片大小，讓它適合畫布的大小
    # Image.LANCZOS 是一種縮放演算法，能讓圖片縮小後更清晰
    image = image.resize((canvas.winfo_width(), canvas.winfo_height()), Image.LANCZOS)

    # 轉換成 tkinter 可以用的格式
    photo = ImageTk.PhotoImage(image)

    # 在畫布上顯示圖片（左上角對齊）
    canvas.create_image(0, 0, anchor="nw", image=photo)

    # 保留圖片，避免被垃圾回收機制刪掉
    canvas.image = photo


#################建立按鈕########################
button = Button(windows, text="按我", command=open_file)
button.grid(row=0, column=2, sticky="W")
button2 = Button(windows, text="按我1", command=show_image)
button2.grid(row=1, column=0, columnspan=3, sticky="EW")
canvas = Canvas(windows, width=600, height=600)
canvas.grid(row=3, column=0, columnspan=3)


windows.mainloop()
