from tkinter import *
import sys
root = Tk()
root.geometry("300x100")
root.title("Message")
root.resizable(False, False)

label_0 = Label(root, text=sys.argv[1], width=20, background="white").place(relx=.50, rely=.50)
exit1 = Button(root, text="Exit", command=root.destroy).pack()

root.mainloop()