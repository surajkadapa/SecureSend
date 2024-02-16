from tkinter import *

def add_button():
    Button(main, text='New Button', command=add_button).pack()

main = Tk()
main_button = Button(main,text='Press to add button',command=add_button).pack()
main.mainloop()