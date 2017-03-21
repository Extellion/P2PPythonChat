# -*- coding: utf-8 -*-

import socket
import time

host = '127.0.0.1'
port = 5000

clients = []

#AF_INET is an address family, when you create a socket, you have to specify its address family, for example unix kernel support 29 other families (AF_UNIX, AF_IPX...)
#SOCK_DGRAM ???????????????????
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(0)

quit = False
print('Server started')

while not quit:
    try:
        #Receive data from the socket. The return value is a pair (bytes, address) where bytes is a bytes object representing the data received and address is the address of the socket sending the data.
        data, addr = s.recvfrom(1024)
        if "end" in str(data):
            quit = True
        #add client address if first connection
        if addr not in clients:
            clients.append(addr)

        print time.ctime(time.time()) + str(addr) + ": :" + str(data)
        for client in clients:
            s.sendto(data, client)
    except:
        pass

s.close()