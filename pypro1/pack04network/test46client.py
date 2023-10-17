# 클라이언트는 일회용
from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('127.0.0.1', 7878))
clientsock.send('국인이 형이야~~'.encode(encoding='utf-8', errors='strict'))
re_msg = clientsock.recv(1024).decode()
print('수신 자료 : ' + re_msg)
clientsock.close()