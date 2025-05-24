from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import mysql.connector as mysql


def game(player1id, player2id, mainwindow):
    window = Toplevel(mainwindow)
    window.geometry("600x300")
    p1 = PhotoImage(file='./turtle/assets/turtle1.png')
    window.iconphoto(False, p1)
    window.title("Turtle Game | VVLC")
    window.focus_force()

    con = mysql.connect(host="localhost", passwd="admin", user="root", database="vvlcdatabase")
    cursor = con.cursor()

    global winner, loser, player1pos, player2pos
    player1pos = 0
    player2pos = 0
    winner = None
    loser = None

    def gameover(winner, loser):
        tkinter.messagebox.showinfo("Game Over", f"{winner} defeated {loser}")
        cursor.execute(f"SELECT * FROM PLAYERINFO WHERE USERNAME = '{winner}'")
        data = cursor.fetchall()
        data = data[0]
        wins = data[4]
        wins = str(wins)
        if wins == "None":
            wins = loser
        else:
            winlst = wins.split(", ")
            if loser not in winlst:
                wins += f", {loser}"
        cursor.execute(f"UPDATE PLAYERINFO SET TURTLEWINS = '{wins}' WHERE USERNAME = '{winner}'")
        con.commit()
        exit()

    def exit():
        window.quit()
        window.destroy()

    def keypress(event):
        global player1pos, player2pos, winner, loser

        if winner == None:
            if event.char == "z":
                canvas.move(player1, 10, 0)
                player1pos += 2
            elif event.char == "m":
                canvas.move(player2, 10, 0)
                player2pos += 2
            if player1pos == 110:
                print("Player 1 Wins")
                winner = player1id
                loser = player2id
                exitbutton.pack()
                gameover(winner, loser)
            elif player2pos == 110:
                print("Player 2 Wins")
                winner = player2id
                loser = player1id
                exitbutton.pack()
                gameover(winner, loser)

    exitbutton = Button(window, text="EXIT", command=exit)
    canvas = Canvas(window, width=600, height=300)
    canvas.pack()

    img1 = Image.open("./turtle/assets/turtle2.png")
    img1 = img1.resize((50, 50))
    img1 = ImageTk.PhotoImage(img1)
    img2 = Image.open("./turtle/assets/turtle3.png")
    img2 = img2.resize((50, 50))
    img2 = ImageTk.PhotoImage(img2)

    img0 = Image.open("./turtle/assets/forestbg.png")
    img0 = img0.resize((600, 300))
    img0 = ImageTk.PhotoImage(img0)
    bgimg = canvas.create_image(300, 150, image=img0)

    player1 = canvas.create_image(20, 80, image=img1)
    player2 = canvas.create_image(20, 150, image=img2)
    canvas.create_line(50, 45, 50, 210, fill="red")
    canvas.create_line(550, 45, 550, 210, fill="red")

    window.bind("<Key>", keypress)

    window.mainloop()
