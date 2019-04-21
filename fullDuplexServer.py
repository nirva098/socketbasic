import socket
import sys
import select

s = socket.socket()

host = socket.gethostbyname(socket.gethostname())

port = 12345
addr = (host,port)
s.bind(addr)
s.listen(1)


c, adr = s.accept()

iobuffer = [c, sys.stdin]


flag = True
while True:
	rs, ws, es = select.select(iobuffer, [], [])
	for r in rs:
		if r is c:
			msg = c.recv(2048).decode()
			print("Friend",":", msg)
			if msg == "q":
				print("This connection is getting terminatted")
				c.send("Thank you for the chat!".encode())
				c.close()
				flag = False
		else:
			c.send(input().encode())
			
		if not (flag):
			break

print("You are out of chat room!")
s.close()
	






