import socket

host = 'localhost'
port = 4000

s = socket.socket()

s.connect((host,port))

msg = s.recv(1024)
while msg:
    print('Received: ',msg.decode())
    msg = s.recv(1024)

s.close()
