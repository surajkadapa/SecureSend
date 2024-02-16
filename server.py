

import tkinter as tk
def getText():
    print("Hello World")
def main():
    root = tk.Tk()
    root.title("SecureSend")
    root.geometry("1000x500")
    root.configure(bg="aqua")
    root.resizable(False, False)

    title = tk.Label(root, bg="aqua", text="SecureSend", font=('Latin Modern Mono', 20))
    title.place(relx=0.5, rely=0.05, anchor='center')

    title = tk.Label(root, bg="aqua", text="Messages Recieved", font=('Latin Modern Mono', 20))
    title.place(relx=0.15, rely=0.2, anchor='center')

    recp_input = tk.Text(root, height=20, width=20)
    recp_input.config(fg="white")
    recp_input.place(relx=0.150, rely=0.600, anchor="center")

    recepient = tk.Label(root, bg="aqua", text="Recepient IP", font=('Latin Modern Mono', 20))
    recepient.place(relx=0.40, rely=0.2, anchor="center")
    
    recp_input = tk.Text(root, height=2, width=40, wrap=tk.WORD)
    recp_input.place(relx=0.71, rely=0.2, anchor="center")
    
    passw = tk.Label(root, bg="aqua", text="Password", font=('Latin Modern Mono', 20))
    passw.place(relx=0.41, rely=0.3, anchor="center")

    recp_input = tk.Text(root, height=2, width=40, wrap=tk.WORD)
    recp_input.place(relx=0.71, rely=0.3, anchor="center")
        
    msg = tk.Label(root, bg="aqua", text="Message", font=('Latin Modern Mono', 20))
    msg.place(relx=0.41, rely=0.5, anchor="center")
    
    recp_input = tk.Text(root, height=10, width=40, wrap=tk.WORD)
    recp_input.place(relx=0.71, rely=0.6, anchor="center")

    send_btn = tk.Button(root, text="Send!", command=getText)
    send_btn.place(relx=.8, rely=.90, anchor="center")
    
    root.mainloop()


if __name__ == '__main__':
    main()