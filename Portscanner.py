import socket

target = input('What is the target IP address?')
startrange = int(input("What is the start of the port range?"))
endrange = int(input("What is the end of the port range?"))


def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

for port in range(startrange, endrange):
    result = portscan(port)
    if result:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
