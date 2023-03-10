import sys
from tkinter import *

frame = Tk()

frame.geometry('450x450+500+200')
frame.title("Learn Tkinter")

lbl = Label(None,text="Hello World",fg = "red", bg = "black")#.pack()
#lbl.pack() center at the top
#lbl.place(x=10,y=50) #placing their position
lbl.grid(row = 0, column = 0, sticky = E) # sticky = N,S,W,E

lb = Label(text = "Bro")
lb.grid(row = 1, column = 0,sticky = E)

#ONLY WINDOWS
frame.mainloop()
#ONLY WINDOWS


print(2**85)
