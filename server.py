import socket

sock = socket.socket()
print ("Socket created successfully.")
port = 8800
host = ''

sock.bind((host, port))

sock.listen(10)
print('Socket is listening...')

while True:
    con, addr = sock.accept()
    print('Connected with ', addr)

    data = con.recv(1024)
    print(data.decode())
    file = open('sample.txt', 'rb')
    line = file.read(1024)
    while(line):
        con.send(line)
        line = file.read(1024)
    
    file.close()
    print('File has been transferred successfully.')
    con.close()