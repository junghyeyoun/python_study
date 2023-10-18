# 클라이언트가 전송한 정보 받기 : get
import cgi

form = cgi.FieldStorage()
irum = form["name"].value + "님"
nai = form["age"].value + "살"

print('Content-Type:text/html;charset=utf-8\n')
print('''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
이름은 {0}, 나이는 {1}
</body>
</html>
''' .format(irum, nai))  
