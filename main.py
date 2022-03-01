from tkinter import *
from PIL import ImageTk, Image
import random
import mysql.connector as mysql

from turtle import turtle
from reflex import reflex

consolewindow = Tk()
consolewindow.title("VVLC Gaming Console")
consolewindow.geometry("600x300")
p1 = PhotoImage(file='./assets/game.png')
consolewindow.iconphoto(False, p1)

con = mysql.connect(host="localhost", passwd="admin", user="root")
cursor = con.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS VVLCDATABASE")
cursor.execute("USE VVLCDATABASE")
cursor.execute("CREATE TABLE IF NOT EXISTS PLAYERINFO (NAME VARCHAR(30), USERNAME VARCHAR(30), PASSWORD VARCHAR(30), REFLEXSCORE INT, TURTLEWINS VARCHAR(255))")
con.commit()

over = False

def loginer(text=None):
    global over

    loginwindow = Toplevel(consolewindow)
    loginwindow.geometry("300x400")
    uname_var = StringVar()
    passw_var = StringVar()

    spassw_var = StringVar()
    suname_var = StringVar()
    sname_var = StringVar()

    def signinfn():
        global over
        over = False

        cursor.execute("SELECT * FROM PLAYERINFO")
        profilelist = cursor.fetchall()

        username = uname_var.get()
        password = passw_var.get()

        print("The username is : " + username)
        print("The password is : " + password)

        uname_var.set("")
        passw_var.set("")

        for i in profilelist:
            if username == i[1] and password == i[2]:
                over = username
        loginwindow.quit()
        loginwindow.destroy()

    def signupfn():
        global over

        over = False
        exists = False

        name = sname_var.get()
        username = suname_var.get()
        password = spassw_var.get()

        print("The username is : " + username)
        print("The name is : " + name)
        print("The password is : " + password)

        suname_var.set("")
        spassw_var.set("")
        sname_var.set("")

        cursor.execute("SELECT * FROM PLAYERINFO")
        profilelist = cursor.fetchall()

        if len(name) > 30 or len(password) > 30 or len(username) > 30 or password == None or name == None or username == None:
            exists = True

        for i in profilelist:
            if username == i[1]:
                exists = True
                break

        if exists == False:
            cursor.execute(f"INSERT INTO PLAYERINFO VALUES('{name}', '{username}', '{password}', 0, 'None')")
            con.commit()

            over = username
        loginwindow.quit()
        loginwindow.destroy()


    txtlabel = Label(loginwindow, text=text, justify="center", font=('calibre', 20, 'bold'))
    txtlabel2 = Label(loginwindow, text="Signin", justify="center", font=('calibre', 20, 'bold'))
    txtlabel3 = Label(loginwindow, text="(OR)", justify="center", font=('calibre', 20, 'bold'))
    txtlabel4 = Label(loginwindow, text="Signup", justify="center", font=('calibre', 20, 'bold'))

    uname_label = Label(loginwindow, text='Username')
    uname_entry = Entry(loginwindow, textvariable=uname_var)
    uname_label2 = Label(loginwindow, text='Username')
    uname_entry2 = Entry(loginwindow, textvariable=suname_var)

    name_label = Label(loginwindow, text='Name')
    name_entry = Entry(loginwindow, textvariable=sname_var)

    passw_label = Label(loginwindow, text='Password')
    passw_entry = Entry(loginwindow, textvariable=passw_var, show='*')
    passw_label2 = Label(loginwindow, text='Password')
    passw_entry2 = Entry(loginwindow, textvariable=spassw_var, show='*')

    signin = Button(loginwindow, text="Signin", command=signinfn)
    signup = Button(loginwindow, text="Signup", command=signupfn)

    txtlabel.pack()
    txtlabel2.pack()
    uname_label.pack()
    uname_entry.pack()
    passw_label.pack()
    passw_entry.pack()
    signin.pack()

    txtlabel3.pack()
    txtlabel4.pack()
    uname_label2.pack()
    uname_entry2.pack()
    name_label.pack()
    name_entry.pack()
    passw_label2.pack()
    passw_entry2.pack()
    signup.pack()
    loginwindow.mainloop()
    return over


def turtlegame():
    player1 = False
    player2 = False

    while player1 == False:
        player1 = loginer(text="Player 1")
    while player2 == False:
        player2 = loginer(text="Player 2")

    turtle.game(player1, player2, consolewindow)


def reflexgame():
    player = False
    while player == False:
        player = loginer(text="Singleplayer")

    reflex.game(1231, consolewindow)


def randomgame():
    randgame = random.choice(["turtle", "reflex"])

    if randgame == "turtle":
        turtlegame()
    elif randgame == "reflex":
        reflexgame()


def exitwindow():
    consolewindow.quit()
    consolewindow.destroy()


def credits():
    window = Toplevel(consolewindow)
    window.geometry("350x325")
    p1 = PhotoImage(file='./assets/game.png')
    window.iconphoto(False, p1)
    window.title("VVLC Creators")

    label1 = Label(window, text="Creators of VVLC", justify="center", font=('calibre', 25, 'bold'))
    label2 = Label(window, text="Vignesh.T.A\nRollno:- 29\n\nV.Viswesh Kissan\nRollno:- 28\n\nV.Lathish\nRollno:- 27\n\nK.Charan\nRollno:- 22", font=('calibre', 15, 'bold'))
    label1.pack()
    label2.pack()


def leaderboard():
    window = Toplevel(consolewindow)
    window.geometry("350x500")
    p1 = PhotoImage(file='./assets/trophy.png')
    window.iconphoto(False, p1)
    window.title("VVLC Leaderboard")

    label3 = Label(window, text="Leaderboard", justify="center", font=('calibre', 20, 'bold'))
    label3.grid(row=0, column=0, columnspan=5)
    label4 = Label(window, text="Rank")
    label4.grid(row=1, column=0, sticky="w")
    label5 = Label(window, text="Name")
    label5.grid(row=1, column=1, sticky="w")
    label6 = Label(window, text="Username")
    label6.grid(row=1, column=2, sticky="w")
    label7 = Label(window, text="Reflex Score")
    label7.grid(row=1, column=3, sticky="w")
    label8 = Label(window, text="Turtle Wins")
    label8.grid(row=1, column=4, sticky="w")

    cursor.execute("SELECT * FROM PLAYERINFO ORDER BY REFLEXSCORE")
    data = cursor.fetchall()

    for i in range(len(data)):
        rec = data[i]
        position = str(i+1)
        name = rec[0]
        username = rec[1]
        reflexscore = rec[3]
        turtlewins = rec[4]

        if i == 0:
            bolder = "bold"
        else:
            bolder = "normal"

        label9 = Label(window, text=position, font=('calibre', 10, bolder))
        label9.grid(row=i+2, column=0)
        label10 = Label(window, text=name, font=('calibre', 10, bolder))
        label10.grid(row=i+2, column=1)
        label11 = Label(window, text=username, font=('calibre', 10, bolder))
        label11.grid(row=i+2, column=2)
        label12 = Label(window, text=str(reflexscore), font=('calibre', 10, bolder))
        label12.grid(row=i+2, column=3)
        label13 = Label(window, text=turtlewins, font=('calibre', 10, bolder))
        label13.grid(row=i+2, column=4)


def documentation():
    window = Toplevel(consolewindow)
    window.geometry("300x600")
    p1 = PhotoImage(file='./assets/documentation.png')
    window.iconphoto(False, p1)
    window.title("VVLC Documentation")

    f = open("README.txt")
    fdata = f.read()
    f.close()
    label1 = Label(window, text="README.txt")
    label2 = Label(window, text=fdata)
    label1.pack()
    label2.pack(anchor="w")


turtlebtn = Button(consolewindow, text="Play Turtle Race", command=turtlegame)
turtlebtn.pack()
wcfbtn = Button(consolewindow, text="Play Reflex Game", command=reflexgame)
wcfbtn.pack()
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

img1 = Image.open("./assets/vvlc.png")
img1 = img1.resize((253, 102), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(img1)
imglabel = Label(consolewindow, image=img1)
imglabel.pack()

consolewindow.mainloop()
con.close()
