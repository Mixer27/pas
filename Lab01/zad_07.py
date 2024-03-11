import socket
import sys

HOST = sys.argv[1]
# PORT = int(sys.argv[2])
# server_address = (HOST, PORT)

# TCP
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.settimeout(0.5)

open_ports = []

for p in range(1, 65535):
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
			sock.settimeout(0.5)
			sock.connect((HOST, p))
			print("Port {} jest otwarty".format(p))
			open_ports.append(p)
	except socket.error as e:
		print("Port {} jest zamknięty".format(p), e)

print("Otwarte porty: ", open_ports)
sock.close()