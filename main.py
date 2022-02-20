from tkinter import *
import random

from turtle import turtle
from wcf import wcf
from ttt import ttt


logedin = 0

consolewindow = Tk()
consolewindow.title("VVLC Gaming Console")
consolewindow.geometry("600x300")
p1 = PhotoImage(file='./assets/game.png')
consolewindow.iconphoto(False, p1)


def loginer(text=None):
    global over
    root = Toplevel(consolewindow)
    root.geometry("300x300")
    name_var = StringVar()
    passw_var = StringVar()

    def submit():
        global over

        username = name_var.get()
        password = passw_var.get()

        username = int(username)

        print("The name is : " + str(username))
        print("The password is : " + password)

        name_var.set("")
        passw_var.set("")
        over = username
        root.quit()
        root.destroy()

    txtlabel = Label(root, text=text, justify="center", font=('calibre', 20, 'bold'))
    name_label = Label(root, text='Username')
    name_entry = Entry(root, textvariable=name_var)
    passw_label = Label(root, text='Password')
    passw_entry = Entry(root, textvariable=passw_var, show='*')
    print(123)
    sub_btn = Button(root, text='Submit', command=submit)
    print(12)
    txtlabel.pack()
    name_label.pack()
    name_entry.pack()
    passw_label.pack()
    passw_entry.pack()
    sub_btn.pack()
    print(1234)

    root.mainloop()

    return over


def turtlegame():
    player1 = loginer(text="Player 1")
    player2 = loginer(text="Player 2")
    winner = turtle.game(player1, player2, consolewindow)
    creditor(winner, 10)

def wcfgame():
    winner = wcf.game(1231, consolewindow)
    creditor(winner, 5)

def tttgame():
    winner = ttt.game(1234, consolewindow)
    creditor(winner, 10)

def randomgame():
    randgame = random.choice(["turtle", "wcf", "ttt"])
    if randgame == "turtle":
        turtlegame()
    elif randgame == "wcf":
        wcfgame()
    elif randgame == "ttt":
        tttgame()


def exitwindow():
    consolewindow.destroy()


def creditor(player, val):
    pass


def credits():
    window = Toplevel(consolewindow)
    window.geometry("300x300")
    p1 = PhotoImage(file='./assets/game.png')
    window.iconphoto(False, p1)
    window.title("VVLC Creators")


def leaderboard():
    window = Toplevel(consolewindow)
    window.geometry("300x300")
    p1 = PhotoImage(file='./assets/trophy.png')
    window.iconphoto(False, p1)
    window.title("VVLC Leaderboard")

def documentation():
    window = Toplevel(consolewindow)
    window.geometry("300x600")
    p1 = PhotoImage(file='./assets/documentation.png')
    window.iconphoto(False, p1)
    window.title("VVLC Leaderboard")

turtlebtn = Button(consolewindow, text="Play Turtle Race", command=turtlegame)
turtlebtn.pack()
wcfbtn = Button(consolewindow, text="Play WCF", command=wcfgame)
wcfbtn.pack()
tttbtn = Button(consolewindow, text="Play TicTacToe", command=tttgame)
tttbtn.pack()
randbtn = Button(consolewindow, text="Random Game", command=randomgame)
randbtn.pack()
creditsbtn = Button(consolewindow, text="Leaderboard", command=leaderboard)
creditsbtn.pack()
leaderboardbtn = Button(consolewindow, text="Credits", command=credits)
leaderboardbtn.pack()
documentationbtn = Button(consolewindow, text="Documentation", command=documentation)
documentationbtn.pack()
exitbtn = Button(consolewindow, text="Exit", command=exitwindow)
exitbtn.pack()

consolewindow.mainloop()
