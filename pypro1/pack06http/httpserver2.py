# 웹서버 (GET, Head, POST 처리) 구축

# CGI : 웹서버와 외부 프로그램 사이에서 정보를 주고 받는 방법이나 규약
# CGIHTTPRequestHandler : 정적 요청 뿐 아니라 동척 요청 처리도 가능
from http.server import CGIHTTPRequestHandler, HTTPServer

port = 8888
class Handler(CGIHTTPRequestHandler):
    cgi_directories = ['/cgi-bin']

serv = HTTPServer(('127.0.0.1', port), Handler)
print('웹 서버 서비스 진행 중 ...')
serv.serve_forever()