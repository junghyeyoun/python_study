# 단순 클라이언트
from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('127.0.0.1', 7878))
clientsock.send('국인이 형이야~~'.encode(encoding='utf-8', errors='strict'))
clientsock.close()