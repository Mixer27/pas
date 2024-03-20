import socket
import sys

HOST = "127.0.0.1"
PORT = 2906
server_address = (HOST, PORT)


ip_address = sys.argv[1].encode()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.settimeout(3)
    try:	
        sock.connect(server_address)
        print("Udane połączenie")
        sock.send(ip_address)
        res = sock.recv(1024)
        print(res.decode())
    except socket.error as e:
        print("Nie udało się połączyć", e)

sock.close()
