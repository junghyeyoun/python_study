# 파이썬 파일로 html 문서 반환
a = 10
b = 20
jumsu = a + b
ss1 = '파이썬'
ss2 = '만세'
print('Content-Type:text/html;charset=utf-8\n')
print('<html><body>')
print('<b>안녕하세요</b> 파이썬 파일로 html문서 작성<br/>')
print('점수 : %d'%(jumsu,))
print('<br>%s %s'%(ss1,ss2))
print('</body></html>')