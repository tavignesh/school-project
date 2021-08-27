import tkinter as tk

window = tk.Tk("halooo")

first = False

def handle_keypress(event):
    global first
    if first == False:
        first = True
        print(f"{event.char} is forst")
        print(f"{event.char} is forst")
    else:
        print("e is last lol")
  
def handle_keypresss(event):
    global first
    if first == False:
        first = True
        print("f is forst")
    else:
        print("f is last lol")
        

#window.bind("e", handle_keypress)
#window.bind("f", handle_keypresss)
window.bind("<Key>", handle_keypress)

window.mainloop()