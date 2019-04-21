import socket

# getting the address
host = socket.gethostbyname(socket.gethostname())
port = 2000
addr = (host, port) # in python, address is a tuple of ip and port number.

# creating a server socket
s = socket.socket()

# binding the socket with server's address
s.bind(addr)

# socket is open for accepting requests 
s.listen(1)

# accepting the request of client
con, adr = s.accept()

print("Message from:",adr,"\n",con.recv(2048).decode())

con.close()
s.close()
