import socket
import sys
import select


# creating a socket for connecting to server
client = socket.socket()

# getting the servers address
host = socket.gethostbyname(socket.gethostname())
port = 12345
addr = (host,port)

# connecting the client socket to server at specified address
client.connect(addr)

iobuffer = [client, sys.stdin]

flag = True

while True:
	rl, wl, el = select.select(iobuffer, [], [])
	for r in rl:
		if r is client:
			msg = client.recv(2048).decode()
			print("Friend:",msg)
			if msg == "q":
				client.send("Thank you for the chat!".encode())
				client.close()
				flag = False
				break
		else:
			client.send(input().encode())
		
		if not (flag):
			break

print("You are out of chat")


	



