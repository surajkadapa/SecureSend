from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter.ttk import *

root = Tk()
root.geometry('280x100')
root.title("Export Status")
root.config(bg="")
style = ttk.Style()


label_0 = Label(root, text="Export Successful", width=20, background="white", foreground="grey15", font=("Arial, bold", 15)).place(x=50, y=23)

exit1 = Button(root, text='Exit', style='C.TButton', width=11, command=root.destroy).place(x=100, y=60)

root.mainloop()