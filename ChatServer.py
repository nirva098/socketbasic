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

print("Server ",s," is listening the requests!")


# accepting the request of client
try:
    con, adr = s.accept()
    print("Connection is established with a client from :",addr)
except:
    print("Unable to connect!")
    exit()
    pass

print("Welcome to sync chat!")
print("Note: \n1.Chat will be initiated by client, so wait for the message\n2.Server and client is supposed to send the messages one by one.")

while True:
    rmsg = con.recv(2048).decode()
    print("client:",rmsg)
    if(rmsg == 'quit' or rmsg == 'leave' or rmsg == 'bye'):
        smsg = "Ok. " + rmsg + " acknowledged!"
        con.send(smsg.encode())
        break
    else:
        smsg = input("server: ")
        con.send(smsg.encode())

con.close()
s.close()


    
