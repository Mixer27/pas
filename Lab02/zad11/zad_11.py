import socket
import sys

HOST = "127.0.0.1"
PORT = 2908
server_address = (HOST, PORT)

# TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)

msg = input()
if (len(msg) <= 20 ):
    msg = msg.ljust(20, " ")
else:
    msg = msg[:20]
# print(len(msg))
msg = msg.encode()
try:	
	sock.connect(server_address)
	print("Udane połączenie")
	sock.send(msg)
	res = sock.recv(1024)
	print(res.decode())
except socket.error as e:
	print("Nie udało się połączyć", e)

sock.close()


