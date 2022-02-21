from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import time
import random

winner = None
loser = None
beforetime = True

def game(player1, player2, mainwindow):
    global winner, loser
    window = Toplevel(mainwindow)
    window.geometry("600x300")
    p1 = PhotoImage(file='./turtle/assets/turtle1.png')
    window.iconphoto(False, p1)
    window.title("Who Clicks First | VVLC")

    exitbutton = Button(window, text="EXIT", command=exit)
    canvas = Canvas(window, width=500, height=250)
    canvas.pack()

    def keypressz(event):
        global loser, winner, beforetime
        if winner == None:
            if beforetime == True:
                winner = player2
                loser = player1
            else:
                winner = player1
                loser = player2
            tkinter.messagebox.showinfo("Game Over", f"{winner} defeated {loser}")

    def keypressm(event):
        global loser, winner, beforetime
        if winner == None:
            if beforetime == True:
                winner = player1
                loser = player2
            else:
                winner = player2
                loser = player1
            tkinter.messagebox.showinfo("Game Over", f"{winner} defeated {loser}")

    def start():
        beforetime = True
        time.sleep(random.randrange(0, 10))
        startimg = canvas.create_image(100, 100, image=img1)
        beforetime = False

    def exit():
        window.quit()
        window.destroy()

    img1 = Image.open("./wcf/assets/start.png")
    img1 = img1.resize((100, 100), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    window.bind("<KeyPress-z>", keypressz)
    window.bind("<KeyPress-m>", keypressm)
    startbtn = Button(window, text="Start", command=start)
    startbtn.pack()
    exitbtn = Button(window, text="Exit", command=exit)
    exitbtn.pack()
    window.mainloop()
