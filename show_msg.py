from tkinter import *
import sys
bg_main = "#1e1f2b"
bg_text = "#9a9aac"
color_text = "#b1b8bc"
root = Tk()
root.geometry("300x100")
root.configure(bg=bg_main)
root.title("Message")
root.resizable(False, False)

msg_rec = Label(root, text=sys.argv[1], font=('Latin Modern Mono',20),bg=bg_main,fg=color_text)
msg_rec.place(relx=0.5,rely=0.2,anchor="center")
exit1 = Button(root, text="Exit", command=root.destroy, bg="red",fg="Black",width=7).place(relx=0.5,rely=0.5,anchor="center")

root.mainloop()