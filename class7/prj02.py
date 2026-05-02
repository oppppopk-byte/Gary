#######################匯入模組#######################
from ttkbootstrap import *
import os
import sys
from PIL import Image, ImageTk

#######################設定工作目錄#######################
os.chdir(sys.path[0])


#######################定義函數#######################
def on_switch_change():
    check_labe1.config(text=str(check_type.get()))


#######################建立視窗#######################
Window = Tk()
Window.title("Checkutton")
#######################設定字形#######################
font_size = 20
Window.option_add("*Font", ("Helvetica", font_size))
#######################設定主題#######################
style = Style(theme="minty")
style.configure("my.TButton", font=("Helvetica", font_size))
style.configure("my.TCheckbutton", font=("Helvetica", font_size))
#######################建立變數#######################
check_labe1 = Label(Window, text="True")
check_labe1.grid(row=1, column=2, padx=10, pady=10)
check_type = BooleanVar(value=True)
#######################建立標籤#######################
check = Checkbutton(
    Window,
    variable=check_type,
    onvalue=True,
    offvalue=False,
    command=on_switch_change,
    style="my.TCheckbutton",
)
check.grid(row=1, column=1, padx=10, pady=10)
image = Image.open("weather.png")
img = ImageTk.PhotoImage(image)
img_label = Label(Window, image=img)
img_label.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
img_label.image = img
#######################運行應運程式#######################
Window.mainloop()
