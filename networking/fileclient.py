import socket

host = 'localhost'
port = 6775

s = socket.socket()

s.connect((host,port))

filename = input('Enter a file name: ')
s.send(filename.encode())
msg = s.recv(1024)
while msg:
    print('Received: ',msg.decode())
    msg = s.recv(1024)

s.close()
