import ipaddress


address = input("Podaj adres IP\n")

def isValidIpAddress(address):
    try:
        ipaddress.ip_address(address=address)
        return True
    except ValueError:
        return False

print("True" if isValidIpAddress(address=address) else "False")