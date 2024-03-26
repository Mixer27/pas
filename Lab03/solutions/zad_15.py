import socket, sys

HOST = '127.0.0.1'
PORT = 2911
server_address = (HOST, PORT)

def decimal_to_ip(d):
    first_octet = d // (256**3)
    r = d % (256**3)
    second_octet = r // (256**2)
    r = r % (256**2)
    third_octet = r // (256**1)
    fourth_octet = r % (256**1)
    
    # Tworzenie stringa adresu IP
    ip_address = f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"
    return ip_address

packet = "45 00 00 4e f7 fa 40 00 38 06 9d 33 d4 b6 18 1b c0 a8 00 02 0b 54 b9 a6 fb f9 3c 57 c1 0a 06 c1 80 18 00 e3 ce 9c 00 00 01 01 08 0a 03 a6 eb 01 00 0b f8 e5 6e 65 74 77 6f 72 6b 20 70 72 6f 67 72 61 6d 6d 69 6e 67 20 69 73 20 66 75 6e"
packet = packet.replace(" ", "")

version = int(packet[0], 16)
src_ip = decimal_to_ip(int(packet[24:32], 16))
dst_ip = decimal_to_ip(int(packet[32:40], 16))
protocol_type = int(packet[18:20], 16)
answerA = "zad15odpA;ver;" + str(version) + ";srcip;" + str(src_ip) + ";dstip;" + str(dst_ip) + ";type;" + str(protocol_type)
print(answerA)

src_port = int(packet[40:44], 16)
dst_port = int(packet[44:48], 16)
data = bytes.fromhex(packet[104:]).decode()
answerB = "zad15odpB;srcport;" + str(src_port) + ";dstport;" + str(dst_port) + ";data;" + data
print(answerB)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.settimeout(3)
    try:	
        sock.connect(server_address)
        print("Udane połączenie")
        sock.send(answerA.encode())
        res = sock.recv(1024).decode()
        print(res)
        if (res == "TAK"):
            sock.send(answerB.encode())
            res = sock.recv(1024).decode()
            print(res)
    except socket.error as e:
        print("Nie udało się połączyć", e)

sock.close()
