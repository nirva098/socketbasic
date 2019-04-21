import socket

# getting the address
'''
As server is hosted in the same system,
we are using this host address.
Else, server's ip address would be used as host
'''
host = socket.gethostbyname(socket.gethostname())

port = 2000

addr = (host, port)

# creating a reciever socket
r = socket.socket()

# making a connection request to the server at addr
r.connect(addr)

msg = "The connection is established!"

r.send(msg.encode())

r.close()
