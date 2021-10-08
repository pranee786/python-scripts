import socket

host = 'localhost'
port = 4000

# Internet Protocol version 4, and TCP IP Protocol connection
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Socket to be binded with the set of host and port
s.bind((host,port))

# Server will start listening to the port
print('Server listening on port: ',port)
s.listen(1)

# Server will accept the client connection when client tries to connect to the server
c,addr = s.accept()

print('Connection from : ',str(addr))

# Server can send information using the connection
# The information should be encoded
c.send(b'Hello, How are you?')
c.send('Bye'.encode())
c.close()
