import tkinter as tk
root = tk.Tk()
root.title("SecureSend")
root.geometry("800x500")
root.configure(bg="aqua")
label = tk.Label(root, bg="aqua", text="SecureSend", font=('Latin Modern Mono',20))
label.place(relx=.5,rely=.05,anchor='center')
root.mainloop()