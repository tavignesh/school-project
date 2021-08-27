from tkinter import *
from PIL import ImageTk,Image
import time


window = Tk()
window.geometry("600x300")
p1 = PhotoImage(file = './assets/turtle1.png')
window.iconphoto(False, p1)
window.title("Turtle Game | By Vignesh.T.A")

player1pos = 0
player2pos = 0
winner = None
loser = None

def gameover(winner, loser):
    winimg = Image.open("./assets/winner.png")
    #winimg = img2.resize((200,50), Image.ANTIALIAS)
    winimg = ImageTk.PhotoImage(winimg)
    canvas.create_image(300, 150, image=winimg)
    pass

def save():
    savebutton["state"] = "disabled"

def exit():
    window.destroy()

def keypress(event):
    global player1pos, player2pos, winner, loser
    print(1)
    if winner == None:
        print(2)
        if event.char == "z":
            canvas.move(player1, 10, 0)
            player1pos += 2
        elif event.char == "m":
            canvas.move(player2, 10, 0)
            player2pos += 2
        if player1pos == 100:
            print("Player 1 Wins")
            winner = 1
            loser = 2
            savebutton.pack()
            exitbutton.pack()
            gameover(winner, loser)
        elif player2pos == 100:
            print("Player 2 Wins")
            winner = 2
            loser = 1
            savebutton.pack()
            exitbutton.pack()
            gameover(winner, loser)

#global button2
savebutton =  Button(window, text="Save", command=save)
#global button1
exitbutton =  Button(window, text="EXIT", command=exit)

canvas = Canvas(window, width = 500, height = 250)
canvas.pack()
img1 = Image.open("./assets/turtle2.png")
img1 = img1.resize((50,50), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)
img2 = Image.open("./assets/turtle3.png")
img2 = img2.resize((50,50), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(img2)
player1 = canvas.create_image(0, 80, image=img1)
player2 = canvas.create_image(0, 150, image=img2)
canvas.create_line(30, 30, 30, 200, fill="red")

window.bind("<Key>", keypress)

window.mainloop()