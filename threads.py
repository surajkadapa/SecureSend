import tkinter as tk
from tkinter import simpledialog
from stegano import lsb
from stegano.lsb import generators
from PIL import Image, ImageDraw, ImageTk
import random
import string
import pyminizip
import socket
import threading
import os
import zipfile
from tooltip import Tooltip
from tkinter import PhotoImage
import shutil
import time

port = 8800
host = ''
host_self = ''
counter = 0
pass1 = ''
curr_counter = 0

def get_host():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    global host_self
    host_self = s.getsockname()[0]
    s.close()

def server():
    global recp_addr
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
            recp_addr = addr
            print("connected with ", addr)
            l = con.recv(1024)
            while(l):
                f.write(l)
                print("receiving.....")
                l = con.recv(1024)
            print("done")
            f.close()
            con.close()
            decrypt(file_name, counter)
            counter +=1 
        else:
            continue

def random_str(n):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
    return res
bg_main = "#1e1f2b"
bg_text = "#9a9aac"
color_text = "#b1b8bc"
def main():
    get_host()
    x = threading.Thread(target=server)
    x.start()
    
    global root
    root = tk.Tk()
    root.title("SecureSend")
    root.geometry("1100x575")
    root.configure(bg=bg_main)
    root.resizable(False, False)
    title = tk.Label(root, bg=bg_main, text="SecureSend", font=('Latin Modern Mono',20), fg=color_text)
    title.place(relx=.5,rely=.05,anchor='center')

    width = 30
    height = 30
    img = Image.open("user.png")
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    image = ImageTk.PhotoImage(img)
    ip_addr = tk.Button(root, text="Ip address", image=image)
    ip_addr.place(relx=0.05, rely=0.03, anchor="center")
    Tooltip(ip_addr, text=host_self, wraplength=150)

    msg_rec = tk.Label(root, bg=bg_main, text="Recieved", font=('Latin Modern Mono',20), fg=color_text)
    msg_rec.place(relx=0.15, rely=0.2, anchor="center")
    global recp_msg
    recp_msg = tk.Text(root, height=20, width=20, wrap=tk.WORD, bg=bg_text, highlightbackground=bg_text, highlightthickness=0)
    recp_msg.place(relx=0.150, rely=0.600, anchor="center")

    recepient = tk.Label(root, bg=bg_main, text="Host", font=('Latin Modern Mono',20), fg=color_text)
    recepient.place(relx=.40, rely=.2, anchor="center")

    global recp_input
    recp_input = tk.Text(root, height=1.45, width=40, wrap=tk.WORD, bg=bg_text, highlightbackground=bg_text, highlightthickness=0)
    recp_input.place(relx = 0.656, rely=.2, anchor="center")

    msg = tk.Label(root, bg=bg_main, text="Message", font=('Latin Modern Mono',20), fg=color_text)
    msg.place(relx=.40, rely=.297, anchor="center")

    global msg_input
    msg_input = tk.Text(root, height=11, width=65, wrap=tk.WORD, bg=bg_text, highlightbackground=bg_text, highlightthickness=0)
    msg_input.place(relx = .747, rely=.44, anchor="center")
    
    passw = tk.Label(root, bg=bg_main, text="Password", font=('Latin Modern Mono',20), fg=color_text)
    passw.place(relx=.4, rely=.709, anchor="center")

    global pass_input
    pass_input = tk.Text(root, height=1.47, width=40, wrap=tk.WORD, bg=bg_text, highlightbackground=bg_text, highlightthickness=0)
    pass_input.place(relx = .655, rely=.709, anchor="center")

    send_btn = tk.Button(root, text="Send!", command=getText)
    send_btn.place(relx=.7, rely=.80, anchor="center")
    
    root.mainloop()

def add_buttons(file_name):
    tk.Button(root, text="test").place(relx=0.150,rely=0.342,anchor="center")

def getText():
    global recp
    recp = recp_input.get(1.0,"end-1c")
    global host
    host = recp
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

filenameinternal = ''

def getPass():
    global pass1
    global filenameinternal
    global curr_counter
    counter = curr_counter
    file_name = filenameinternal
    userinp = simpledialog.askstring(title="Password",prompt="password")
    pass1 = userinp
    os.mkdir("get"+str(counter))
    print(os.getcwd())
    with zipfile.ZipFile(file_name) as zf:
        zf.extractall("get"+str(counter)+"/",pwd=bytes(pass1,'utf-8'))
    file_name = file_name.removesuffix('.zip')
    print(os.getcwd()+"/get"+str(counter))
    l = os.listdir(os.getcwd()+"/get"+str(counter))
    fin_file = l[0]
    msg = lsb.reveal(os.getcwd()+"/"+file_name+"/"+fin_file, generators.eratosthenes())
    os.system("python3 show_msg.py \""+msg+"\"")
    shutil.rmtree("get"+str(counter), ignore_errors=True)
    print(msg)

def decPass(file_name):
    global counter
    global filenameinternal
    global recp_addr
    addr = recp_addr
    filenameinternal = file_name
    x = (.072*(counter+1))
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    tk.Button(root, text=str(addr[0])+"|"+str(current_time), command=getPass).place(relx=0.150,rely=(0.27+x),anchor="center")

def decrypt(file_name, curr_counter1):
    global curr_counter
    curr_counter = curr_counter1
    global pass1
    decPass(file_name) 
    

if __name__ == '__main__':
    main()