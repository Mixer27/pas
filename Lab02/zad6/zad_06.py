import socket
import sys

HOST = "127.0.0.1"
PORT = 2902
server_address = (HOST, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.settimeout(3)
    try:	
        sock.connect(server_address)
        print("Udane połączenie")
        while (True):
            user_input = input("Podaj <liczba> <operator> <liczba>\n")
            data1, op, data2 = user_input.split(" ")
            sock.sendto(data1.encode(), server_address)
            sock.sendto(op.encode(), server_address)
            sock.sendto(data2.encode(), server_address)
            res = sock.recv(4096)
            print(res.decode())
    except socket.error as e:
        print("Nie udało się połączyć", e)

sock.close()
