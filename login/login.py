from tkinter import *

def getpass():
    global username_entry
    username = username_entry.get()
    # userusernameh = username_entry.get()
    # check here
    if False:
        pass
    else:
        userpassword = None
        password_entry = Entry(loginwindow, textvariable=userpassword)
        password_entry.pack()
    return [userpassword, userwins, loses]


def login(window):
    return
    global loginwindow
    loginwindow = Toplevel(window)
    window.title("Login | VVLC")
    global username_entry
    userwins = 0
    userloses = 0
    Label(loginwindow, text="Username").pack()
    userusername = None
    username_entry = Entry(loginwindow, textvariable=userusername)
    username_entry.pack()

    Button(loginwindow, text="Next", command=getpass).pack()
    # if username not avaiable:
    #     Label(window, text="The Username You Entered has already been taken or does not exist", foreground="red").pack()
    #     loginwindow.destroy()
    print(userusername)
    print(userpassword)
    return [userusername, userwins, userloses]
