from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Calvin')
window.geometry('400x150')

l1 = Label(window, text='Username', font=(14))
l2 = Label(window, text='Password', font=(14))
l1.grid(row=0, column=0, padx=5, pady=5)
l2.grid(row=1, column=0, padx=5, pady=5)

username = StringVar()
password = StringVar()
t1 = Entry(window, textvariable=username, font=(14))
t2 = Entry(window, textvariable=password, font=(14), show='*')
t1.grid(row=0, column=1)
t2.grid(row=1, column=1)


def login():
    if username.get() == 'calvin' and password.get() == 'audition':
        messagebox.showinfo(title='Login Status', message='Login Success!')
    else:
        messagebox.showerror(title='Login Error',message='Incorrect Credentials')


def cancel():
    status = messagebox.askyesno(
        title='Question', message='Are you sure to close the windows?')
    if status:
        window.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the login menu.')


b1 = Button(window, command=login, text='Login', font=(14))
b2 = Button(window, command=cancel, text='Cancel', font=(14))

b1.grid(row=2, column=1, sticky=W)
b2.grid(row=2, column=1, sticky=E)

window.mainloop()
