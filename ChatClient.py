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
try:
    r.connect(addr)
    print("Connection has established to server on address :",addr)
except:
    print("Connection failed")
    exit()

print("Note: \n1.Client needs to initiate the chat \n2.Server and client is supposed to send the messages one by one.")
while True:
    smsg = input("client: ")
    r.send(smsg.encode())
    rmsg = r.recv(2048).decode()
    print("server:",rmsg)
    if(smsg == 'quit' or smsg == 'leave' or smsg == 'bye'):
        break
r.close()
