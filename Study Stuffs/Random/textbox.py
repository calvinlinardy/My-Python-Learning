from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Calvin')
window.geometry('400x150')

l1 = Label(window, text='Username', font=(14))
l2 = Label(window, text='Password', font=(14))
l1.grid(row=0, column=0, padx=5, pady=5)
l2.grid(row=0, column=0, padx=5, pady=5)

username = StringVar()
password = StringVar()
t1 = Entry(window, textvariable=username, font=(14))
t2 = Entry(window, textvariable=password, font=(14), show='*')
t1.grid(row=0, column=1)
t2.grid(row=1, column=1)
