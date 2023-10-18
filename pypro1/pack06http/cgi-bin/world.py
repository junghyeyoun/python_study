str1 = "파이썬"
str2 = "모듈의"
str3 = "멤버"

print('Content-Type:text/html;charset=utf-8\n')
print('''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h1>world 문서</h1>
자료 출력 : {0} <br/>
{1} 
{2}
<hr/>
<img src='../images/kuromi.jpg' width=80% />
<br/>
<a href='../index.html'>메인으로</a>
</body>
</html>
'''.format(str1,str2,str3))
