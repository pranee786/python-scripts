import socket

host = 'localhost'
port = 6775

# Internet Protocol version 4, and TCP IP Protocol connection
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Socket to be binded with the set of host and port
s.bind((host,port))

# Server will start listening to the port
print('Server listening on port: ',port)
s.listen()

# Server will accept the client connection when client tries to connect to the server
c,addr = s.accept()

filename = c.recv(1024)
try:
    f = open(filename,"rb")
    content = f.read()
    c.send(content)
    f.close()
except FileNotFoundError:
    c.send(b'File does not exist')

c.close()
