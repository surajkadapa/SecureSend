import tkinter as tk
from stegano import lsb
from stegano.lsb import generators
from PIL import Image, ImageDraw
import random
import string
import pyminizip
import socket

def random_str(n):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
    return res

def main():
    root = tk.Tk()
    root.title("SecureSend")
    root.geometry("1000x500")
    root.configure(bg="aqua")
    root.resizable(False, False)
    title = tk.Label(root, bg="aqua", text="SecureSend", font=('Latin Modern Mono',20))
    title.place(relx=.5,rely=.05,anchor='center')
    recepient = tk.Label(root, bg="aqua", text="Recepient IP", font=('Latin Modern Mono',20))
    recepient.place(relx=.157, rely=.157, anchor="center")
    global recp_input
    recp_input = tk.Text(root, height=1.45, width=40, wrap=tk.WORD)
    recp_input.place(relx = .46, rely=.157, anchor="center")
    msg = tk.Label(root, bg="aqua", text="Message", font=('Latin Modern Mono',20))
    msg.place(relx=.157, rely=.297, anchor="center")
    global msg_input
    msg_input = tk.Text(root, height=11, width=65, wrap=tk.WORD)
    msg_input.place(relx = .547, rely=.44, anchor="center")
    passw = tk.Label(root, bg="aqua", text="Password", font=('Latin Modern Mono',20))
    passw.place(relx=.157, rely=.709, anchor="center")
    global pass_input
    pass_input = tk.Text(root, height=1.47, width=40, wrap=tk.WORD)
    pass_input.place(relx = .46, rely=.709, anchor="center")
    send_btn = tk.Button(root, text="Send!", command=getText)
    send_btn.place(relx=.7, rely=.80, anchor="center")
    root.mainloop()


def getText():
    global recp
    recp = recp_input.get(1.0,"end-1c")
    global msg 
    msg = msg_input.get(1.0,"end-1c")
    global passw
    passw = pass_input.get(1.0,"end-1c")
    print(recp, msg, passw)
    encImg()

def createImg():
    width, height = 600, 600
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    for _ in range(1000):
        x = random.randint(0, width-1)
        y = random.randint(0, height-1)
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        draw.point((x,y), fill = color)
    
    res = random_str(7)
    image.save(res+".png")
    return (res+".png")

def encImg():
    img_name = createImg()
    img = lsb.hide(img_name, msg, generators.eratosthenes())
    res = random_str(6)
    img.save(res+".png")
    encZip(res+".png")

def encZip(img_name):
    rand_name = random_str(8)+".zip"
    pyminizip.compress(img_name,None,rand_name,passw,1)
    print(rand_name)
    sendFile(rand_name)

def sendFile(file_name):
    s = socket.socket()
    print("socket created successfully")
    port = 8800
    host = '192.168.122.76'
    s.connect((host, port))
    f = open(file_name,'rb')
    l = f.read(1024)
    while(l):
        s.send(l)
        print("sending...")
        l = f.read(1024)
    print("done")
    f.close()
    s.close()




if __name__ == '__main__':
    main()
