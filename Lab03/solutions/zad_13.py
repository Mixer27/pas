import socket, sys

HOST = '127.0.0.1'
PORT = 2909
server_address = (HOST, PORT)

segment = "0b 54 89 8b 1f 9a 18 ec bb b1 64 f2 80 18 00 e3 67 71 00 00 01 01 08 0a 02 c1 a4 ee 00 1a 4c ee 68 65 6c 6c 6f 20 3a 29"
segment = segment.replace(" ", "")
print(segment)
src_port = int(segment[:4], 16)
dst_port = int(segment[4:8], 16)
data = bytes.fromhex(segment[64:])
data = data.decode()
print(src_port, dst_port, data)
answer = "zad13odp;src;" + str(src_port) + ";dst;" + str(dst_port) + ";data;" + data
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
