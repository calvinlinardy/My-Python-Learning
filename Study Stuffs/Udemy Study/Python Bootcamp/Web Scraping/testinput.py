from tkinter import *
from tkinter import messagebox
from tkinter import font

from pyparsing import col

gui = Tk()
gui.title('TEST')
gui.geometry('200x100')

path = ''

def get_path():
    path = t1.get()
    print(path)

l1 = Label(gui, text='Test', font=(14))
l1.grid(row=0, column=0)

t1 = Entry(gui, textvariable=path, font=(14))
t1.grid(row=0, column=1)

b1 = Button(gui, command=get_path, text='enter', font=(14))
b1.grid(row=1,column=0)

gui.mainloop()