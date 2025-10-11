from tkinter import *
from tkinter import messagebox

from cv2 import meanShift

gui = Tk()
gui.title('XX')
gui.geometry('100x100')

def show():
    messagebox.showinfo(title='TEST',message='WTF man')

start_button = Button(gui, command=show, text='START', font=(14), bg='red')
start_button.grid(row=1, column=1, sticky=W)

gui.mainloop()