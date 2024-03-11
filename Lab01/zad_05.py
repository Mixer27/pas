import sys
import socket

hostname = sys.argv[1]

def get_address(hostname):
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return "Nie można donaleźć adresu dla wskazanej nazwy hosta"

print(get_address(hostname=hostname))