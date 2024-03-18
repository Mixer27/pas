import socket
import sys

HOST = "127.0.0.1"
PORT = 2901
server_address = (HOST, PORT)

msg = "hello from client".encode()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.settimeout(3)
    try:	
        sock.connect(server_address)
        print("Udane połączenie")
        while (True):
            msg = input("Write a message to server\n")
            if (msg == "!stop"):
                break
            else:
                sock.send(msg.encode())
                res = sock.recv(1024)
                print(res)
    except socket.error as e:
        print("Nie udało się połączyć", e)

sock.close()
