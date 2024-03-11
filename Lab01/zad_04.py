import sys
import socket

address = sys.argv[1]

def get_hostname(address):
    try:
        return socket.gethostbyaddr(address)[0]
    except socket.gaierror:
        return "Nie można donaleźć nazwy hostav dla wskazanego adresu"

print(get_hostname(address=address))