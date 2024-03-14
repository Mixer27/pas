import socket
import sys
import struct
import time

HOST = "ntp.task.gda.pl"
PORT = 123
server_address = (HOST, PORT)

# TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)
message = '\x1b' + 47 * '\0'
message = message.encode()

try:	
	# sock.connect(server_address)
	sock.sendto(message, server_address)
	print("Udane połączenie")
	data, _ = sock.recvfrom(1024)
except socket.error as e:
	print("Nie udało się połączyć", e)

t = struct.unpack("!12I", data)[10]
t -= 2208988800

print(time.ctime(t))

