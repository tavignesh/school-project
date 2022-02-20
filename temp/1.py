from tkinter import *

tk=Tk()
tk.withdraw()

d=DoubleVar(master=tk, value=0)

def my_event_handler(*args):
    print(12)

d.trace(mode="w", callback=my_event_handler)

d.set(5.55)
d.set(15.12)
