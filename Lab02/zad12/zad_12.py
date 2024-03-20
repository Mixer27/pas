import socket
import sys

HOST = "127.0.0.1"
PORT = 2908
server_address = (HOST, PORT)

MAX_PACKET_LENGTH = 20

def recvall(sock, msgLen):
    msg = b""
    bytesRcvd = 0

    while bytesRcvd < msgLen:

        chunk = sock.recv(msgLen - bytesRcvd)

        if not chunk:
            break

        bytesRcvd += len(chunk)
        msg += chunk

    return msg


# TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(3)

msg = input()
if (len(msg) <= MAX_PACKET_LENGTH ):
    msg = msg.ljust(MAX_PACKET_LENGTH, " ")
else:
    msg = msg[:MAX_PACKET_LENGTH]
# print(len(msg))
msg = msg.encode()
try:	
	sock.connect(server_address)
	print("Udane połączenie")
	sock.sendall(msg)
	res = recvall(sock, MAX_PACKET_LENGTH)
	print(res.decode())
except socket.error as e:
	print("Nie udało się połączyć", e)

sock.close()


