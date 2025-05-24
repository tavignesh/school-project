from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import random
import time
import mysql.connector as mysql

rt = 1
point = 0
loop = 0


def game(player1, mainwindow):
    global point

    timer = time.time()
    window = Toplevel(mainwindow)
    window.geometry("600x200")
    p1 = PhotoImage(file='./turtle/assets/turtle1.png')
    window.iconphoto(False, p1)
    window.title("Reflex Game | VVLC")

    con = mysql.connect(host="localhost", passwd="admin", user="root", database="vvlcdatabase")
    cursor = con.cursor()

    def change():
        global rt, loop, point

        print(point)
        loop += 1

        if (time.time() - timer) > 20:
            gameover()
        else:
            tt = random.choice([i1_label, i2_label, i3_label, i4_label])

            if tt == i1_label:
                rt = 1
                i1_label.configure(image=img1)
                i2_label.configure(image=img2)
                i3_label.configure(image=img2)
                i4_label.configure(image=img2)
            elif tt == i2_label:
                rt = 2
                i1_label.configure(image=img2)
                i2_label.configure(image=img1)
                i3_label.configure(image=img2)
                i4_label.configure(image=img2)
            elif tt == i3_label:
                rt = 3
                i1_label.configure(image=img2)
                i2_label.configure(image=img2)
                i3_label.configure(image=img1)
                i4_label.configure(image=img2)
            elif tt == i4_label:
                rt = 4
                i1_label.configure(image=img2)
                i2_label.configure(image=img2)
                i3_label.configure(image=img2)
                i4_label.configure(image=img1)

    def gameover():
        global point

        tkinter.messagebox.showinfo("Game Over", f"Points: {point}")

        cursor.execute(f"SELECT * FROM PLAYERINFO WHERE USERNAME = '{player1}'")
        data = cursor.fetchall()
        print(data)
        data = data[0]
        score = int(data[3])
        if point > score:
            cursor.execute(f"UPDATE PLAYERINFO SET REFLEXSCORE = {point} WHERE USERNAME = '{player1}'")
            con.commit()
            con.close()
        point = 0
        exit()

    def exit():
        window.quit()
        window.destroy()

    def img1fn():
        global rt, point

        if rt == 1:
            point += 1
        change()

    def img2fn():
        global rt, point

        if rt == 2:
            point += 1
        change()

    def img3fn():
        global rt, point

        if rt == 3:
            point += 1
        change()

    def img4fn():
        global rt, point

        if rt == 4:
            point += 1
        change()

    img1 = Image.open("./reflex/assets/turtle1.png")
    img1 = img1.resize((80, 80))
    img1 = ImageTk.PhotoImage(img1)
    img2 = Image.open("./reflex/assets/turtle3.png")
    img2 = img2.resize((80, 80))
    img2 = ImageTk.PhotoImage(img2)

    i1_label = Label(window, image=img1)
    i1_label.grid(row=0, column=0)
    i1_btn = Button(window, text="⬆", width=20, height=5, command=img1fn)
    i1_btn.grid(row=1, column=0)
    i2_label = Label(window, image=img2)
    i2_label.grid(row=0, column=2)
    i2_btn = Button(window, text="⬆", width=20, height=5, command=img2fn)
    i2_btn.grid(row=1, column=2)
    i3_label = Label(window, image=img2)
    i3_label.grid(row=0, column=3)
    i3_btn = Button(window, text="⬆", width=20, height=5, command=img3fn)
    i3_btn.grid(row=1, column=3)
    i4_label = Label(window, image=img2)
    i4_label.grid(row=0, column=4)
    i4_btn = Button(window, text="⬆", width=20, height=5, command=img4fn)
    i4_btn.grid(row=1, column=4)

    change()

    exitbutton = Button(window, text="EXIT", command=exit)
    exitbutton.grid(row=4, column=2)

    window.mainloop()
    return point
