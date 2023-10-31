# BeautifulSoup fine, select 연습
from bs4 import  BeautifulSoup
htmlData = """
<html>
<body>
<h1>제목 태그</h1>
<p>문단 1</p>
<p>문단 2</p>
</body>
</html>
"""
print(type(htmlData)) # <class 'str'>
soup = BeautifulSoup(htmlData, 'html.parser') # BeautifulSoup  객체 생성 - BeautifulSoup 모듈 지원 명령 사용 가능
print(type(soup))
h1 = soup.html.body.h1
print('h1 : ',h1.text,' ',h1.string)
p1 = soup.html.body.p
print('p1 : ',p1.text)
p2 = p1.next_sibling.next_sibling
print('p2 : ',p2.text)

print('\n find함수(반환값 1개) 사용 ------------------------------------')
htmlData2 = """
<html>
<body>
<h1 id="title">제목 태그</h1>
<p>문단 1</p>
<p id="my" class="our">문단 2</p>
</body>
</html>
"""
soup2 = BeautifulSoup(htmlData2, 'html.parser')
print(soup2.p, ' ',soup2.string)
print(soup2.find('p' ).string)
print(soup2.find('p' ,id='my').string)
print(soup2.find(id='title').string)
print(soup2.find(id='my').string)
print(soup2.find(class_ ='our').string) # 클래스는 언더바 써야함 !
print(soup2.find(attrs={'class':'our'}).string)
print(soup2.find(attrs={'id':'my'}).string)

print('\n find_all() : 반환 값이 복수 일 경우 사용 ------------------------------------')
htmlData3 = """
<html>
<body>
<h1 id="title">제목 태그</h1>
<p>문단 1</p>
<p id="my" class="our">문단 2</p>
<div>
    <a href="https://www.naver.com">네이버</a><br>
    <a href="https://www.daum.com">다음</a><br>
</div>
</body>
</html>
"""

soup3 = BeautifulSoup(htmlData3, 'lxml')

# 모든 <a> 태그를 찾습니다.
print(soup3.find_all("a"))

# class="our"을 가진 모든 <p> 태그를 찾습니다.
print(soup3.find_all("p", class_="our"))

# 모든 <a> 태그를 찾습니다.
links = soup3.find_all("a")
for i in links:
    if i.string is not None:
        href = i.attrs['href']
        text = i.string
        print(href, text)


print('\n정규 표현식 사용')
import re
links2 = soup3.find_all(href=re.compile(r'^https'))
for j in links2:
    print(j.attrs['href'])