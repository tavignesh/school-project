from tkinter import *
import random

from turtle import turtle
from login import login
from wcf import wcf
from ttt import ttt


logedin = 0

consolewindow = Tk()
consolewindow.title("VVLC Gaming Console")
consolewindow.geometry("600x300")
p1 = PhotoImage(file='./assets/game.png')
consolewindow.iconphoto(False, p1)


def loginer():
    login_info = login.login(consolewindow)
    loginbtn["state"] = "disabled"
    tttbtn["state"] = "normal"
    wcfbtn["state"] = "normal"
    turtlebtn["state"] = "normal"
    return login_info


def turtlegame():
    player1 = loginer()
    player2 = loginer()
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
    window.title("VVLC Creaators")


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
turtlebtn["state"] = "disabled"
wcfbtn = Button(consolewindow, text="Play WCF", command=wcfgame)
wcfbtn.pack()
wcfbtn["state"] = "disabled"
tttbtn = Button(consolewindow, text="Play TicTacToe", command=tttgame)
tttbtn.pack()
tttbtn["state"] = "disabled"
loginbtn = Button(consolewindow, text="Login", command=loginer)
loginbtn.pack()
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
