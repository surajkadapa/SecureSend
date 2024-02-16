import socket
s=socket.socket()
host =
port=
s.bind
f = open('get.zip','wb')
s.listen()
while(True):
    c,addr = s.accept()
    print("Recieved")
    l=c.recv(1024)
    while(l):
        f.write(l)
        print("Recieved")
        l=c.recv(1024)
    f.close()
    c.close()