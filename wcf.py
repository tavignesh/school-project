from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import random

def game(player1, mainwindow):
    window = Toplevel(mainwindow)
    window.geometry("600x300")
    p1 = PhotoImage(file='./turtle/assets/turtle1.png')
    window.iconphoto(False, p1)
    window.title("Reflex Game | VVLC")

    # def change():
    #     photo1 = ImageTk.PhotoImage(Image.open("demo.jpg"))
    #     labelname.configure(image=photo1)

    def exit():
        window.quit()
        window.destroy()

    exitbutton = Button(window, text="EXIT", command=exit)
    canvas = Canvas(window, width=500, height=250)
    canvas.pack()
    img1 = Image.open("./turtle/assets/turtle2.png")
    img1 = img1.resize((80, 80), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    img2 = Image.open("./turtle/assets/turtle3.png")
    img2 = img2.resize((80, 80), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    img3 = Image.open("./turtle/assets/turtle3.png")
    img3 = img3.resize((80, 80), Image.ANTIALIAS)
    img3 = ImageTk.PhotoImage(img3)
    img1_label = Label(window, image=img1)
    img1_label.grid()
    window.mainloop()
