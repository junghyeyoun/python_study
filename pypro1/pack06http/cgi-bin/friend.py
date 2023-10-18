# 클라이언트가 전송한 정보 받기 : post

import cgi

form = cgi.FieldStorage() #dict 형식으로 결과 받음

name = form["name"].value
phone = form["phone"].value
gen = form["gen"].value

print('Content-Type:text/html;charset=utf-8\n')
print('''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
친구 이름은 {0}, 전화는 {1}, 성별은 {2}
</body>
</html>
''' .format(name, phone,gen))  