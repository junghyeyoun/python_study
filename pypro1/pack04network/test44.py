# Network
# socket : 네트워크를 위한 통신 채널을 지원
import socket 

print(socket.getservbyname('http','tcp')) # 80
print(socket.getservbyname('https','tcp')) # 443
print(socket.getservbyname('telnet','tcp'))
print(socket.getservbyname('ftp','tcp'))
print(socket.getservbyname('smtp','tcp'))
print(socket.getservbyname('pop3','tcp'))

print(socket.getaddrinfo('www.naver.com',80,proto=socket.SOL_TCP))
# '223.130.195.95    223.130.195.200 => 주소 치면 naver로 이동
# http://223.130.195.200:80/index.html => url