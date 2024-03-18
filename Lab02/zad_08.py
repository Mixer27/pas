import socket
import sys

services  = {}
with open("services.txt", "r") as f:
    for line in f:
        key, value = line.split(": ")
        services[key] = value.strip("\n")

HOST = sys.argv[1]

open_ports = []

for p in range(1, 65535):
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
			sock.settimeout(0.2)
			sock.connect((HOST, p))
			print("Port {} jest otwarty".format(p))
			print(f"Pzewidyawana usługa na porcie {p}: {services[str(p)]}" )
			open_ports.append(p)
	except socket.error as e:
		print("Port {} jest zamknięty".format(p), e)

print("Otwarte porty: ", open_ports)
sock.close()