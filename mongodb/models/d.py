# from socket import socket, AF_INET, SOCK_DGRAM
# s = socket(AF_INET, SOCK_DGRAM)
# s.bind(('192.168.3.148', 0)) # OS chooses port
# server = ('192.168.0.144', 2000)
# s.sendto(b"qa automation rules!", server)
# data, addr = s.recv(1024)
# s.close()

my_obj = {
    'command': 'list',
}


import json
import socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('192.168.3.148', 0))
    # s.connect(('192.168.0.114', 2000))
    server = ('192.168.0.114', 2000)
    s.sendto(json.dumps(my_obj).encode(), server)
    data, addr = s.recvfrom(1024)
    print(data, addr)