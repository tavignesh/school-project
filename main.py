from tkinter import *
import time

from turtle import turtle
from login import login

logedin = 0

consolewindow = Tk()
consolewindow.title("VVLC Gaming Console")
consolewindow.geometry("600x300")


def loginer():
    login_info = login.login(consolewindow)
    loginbtn["state"] = "disabled"
    return login_info


def turtlegame():
    turtle.turtlegame(1232, consolewindow)


def flappygame():
    pass


def wclgame():
    pass


def tttgame():
    pass


def crediter():
    pass


flappybtn = Button(consolewindow, text="Play Flappy Bird", command=flappygame)
flappybtn.pack()
flappybtn["state"] = "disabled"
turtlebtn = Button(consolewindow, text="Play Turtle Race", command=turtlegame)
turtlebtn.pack()
turtlebtn["state"] = "disabled"
wclbtn = Button(consolewindow, text="Play WCL", command=wclgame)
wclbtn.pack()
wclbtn["state"] = "disabled"
snakebtn = Button(consolewindow, text="Play Snake", command=snakegame)
snakebtn.pack()
snakebtn["state"] = "disabled"
tttbtn = Button(consolewindow, text="Play TicTacToe", command=tttgame)
tttbtn.pack()
tttbtn["state"] = "disabled"
loginbtn = Button(consolewindow, text="Login", command=loginer)
loginbtn.pack()
creditsbutton = Button(consolewindow, text="Credits", command=crediter)
creditsbutton.pack()

consolewindow.mainloop()
