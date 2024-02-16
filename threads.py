import tkinter as tk
from stegano import lsb
from stegano.lsb import generators
from PIL import Image, ImageDraw
import random
import string
import pyminizip
import socket
import threading
import os

port = 8800
host = ''
host_self = ''
counter = 0

def get_host():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    global host_self
    host_self = s.getsockname()[0]
    s.close()

def server():
    global counter
    sock = socket.socket()
    sock.bind((host_self, port))
    sock.listen()
    print("socket is listening")
    while True:
        if(1 == 1):
            file_name = "get"+str(counter)+".zip"
            f = open(file_name,'wb')
            con, addr = sock.accept()
            print("connected with ", addr)
            l = con.recv(1024)
            while(l):
                f.write(l)
                print("receiving.....")
                l = con.recv(1024)
            print("done")
            f.close()
            con.close()
            #decrypt(file_name)
            counter +=1 
        else:
            continue

def random_str(n):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
    return res

def main():
    get_host()
    x = threading.Thread(target=server)
    x.start()
    
    global root
    root = tk.Tk()
    root.title("SecureSend")
    root.geometry("1100x575")
    root.configure(bg="aqua")
    root.resizable(False, False)
    title = tk.Label(root, bg="aqua", text="SecureSend", font=('Latin Modern Mono',20))
    title.place(relx=.5,rely=.05,anchor='center')

    msg_rec = tk.Label(root, bg="aqua", text="Messages recieved", font=('Latin Modern Mono',20))
    msg_rec.place(relx=0.15, rely=0.2, anchor="center")
    global recp_msg
    recp_msg = tk.Text(root, height=20, width=20, wrap=tk.WORD)
    recp_msg.place(relx=0.150, rely=0.600, anchor="center")

    recepient = tk.Label(root, bg="aqua", text="Recepient IP", font=('Latin Modern Mono',20))
    recepient.place(relx=.40, rely=.2, anchor="center")

    global recp_input
    recp_input = tk.Text(root, height=1.45, width=40, wrap=tk.WORD)
    recp_input.place(relx = 0.71, rely=.2, anchor="center")

    msg = tk.Label(root, bg="aqua", text="Message", font=('Latin Modern Mono',20))
    msg.place(relx=.40, rely=.297, anchor="center")

    global msg_input
    msg_input = tk.Text(root, height=11, width=65, wrap=tk.WORD)
    msg_input.place(relx = .747, rely=.44, anchor="center")
    
    passw = tk.Label(root, bg="aqua", text="Password", font=('Latin Modern Mono',20))
    passw.place(relx=.4, rely=.709, anchor="center")

    global pass_input
    pass_input = tk.Text(root, height=1.47, width=40, wrap=tk.WORD)
    pass_input.place(relx = .76, rely=.709, anchor="center")

    send_btn = tk.Button(root, text="Send!", command=add_buttons)
    send_btn.place(relx=.7, rely=.80, anchor="center")
    
    root.mainloop()

def add_buttons():
    tk.Button(root, text="test").place(relx=0.150,rely=0.342,anchor="center")
    tk.Button(root, text="test1").place(relx=0.150,rely=0.41,anchor="center")

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

# def decrypt(file_name):
#     pass = decPass(file_name) #need to implement
#     pyminizip.uncompress(file_name,pass,None,0)
#     file_name = file_name.removesuffix('.zip')
#     l = os.listdir(file_name)
#     fin_file = l[0]
#     msg = lsb.reveal(os.getcwd()+"/"+file_name+"/"+fin_file, generators.eratosthenes())
#     return msg

if __name__ == '__main__':
    main()