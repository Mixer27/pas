import socket
import sys

HOST = "127.0.0.1"
PORT = 2907
server_address = (HOST, PORT)


hostname = sys.argv[1].encode()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.settimeout(3)
    try:	
        sock.connect(server_address)
        print("Udane połączenie")
        sock.send(hostname)
        res = sock.recv(1024)
        print(res.decode())
    except socket.error as e:
        print("Nie udało się połączyć", e)

sock.close()
