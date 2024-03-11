import socket
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])
server_address = (HOST, PORT)

# TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)

try:	
	sock.connect(server_address)
	print("Udane połączenie")
except socket.error as e:
	print("Nie udało się połączyć", e)

sock.close()
