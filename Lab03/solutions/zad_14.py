import socket, sys

HOST = '127.0.0.1'
PORT = 2910
server_address = (HOST, PORT)

datagram = "ed 74 0b 55 00 24 ef fd 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 6e 20 70 79 74 68 6f 6e 20 69 73 20 66 75 6e"
datagram = datagram.replace(" ", "")
print(datagram)
src_port = int(datagram[:4], 16)
dst_port = int(datagram[4:8], 16)
data = bytes.fromhex(datagram[16:])
data = data.decode()
print(src_port, dst_port, data)
answer = "zad14odp;src;" + str(src_port) + ";dst;" + str(dst_port) + ";data;" + data
print(answer)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.settimeout(3)
    try:	
        sock.connect(server_address)
        print("Udane połączenie")
        sock.send(answer.encode())
        res = sock.recv(1024)
        print(res.decode())
    except socket.error as e:
        print("Nie udało się połączyć", e)

sock.close()
