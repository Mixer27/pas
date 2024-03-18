import socket
import sys

services  = {}
with open("services.txt", "r") as f:
    for line in f:
        key, value = line.split(": ")
        services[key] = value.strip("\n")

HOST = sys.argv[1]
PORT = int(sys.argv[2])
server_address = (HOST, PORT)

# TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(4)

try:	
	sock.connect(server_address)
	print("Udane połączenie")
	print(f"Pzewidyawana usługa na porcie {PORT}: {services[str(PORT)]}" )
except socket.error as e:
	print("Nie udało się połączyć", e)

sock.close()
