# 정규 표현식 : 특정한 규칙을 가진 문자열의 집합을 표현하기 위해 쓰이는 형식언어
import re

ss = "1234 abc가나다abcABC_123555_6python si fun파이썬 만세"
print(ss)
print(re.findall(r'123', ss))
print(re.findall(r'가나',ss))

print(re.findall(r'[1,2,5]',ss))
print(re.findall(r'[1,2,5]+',ss)) # 반복 관련 메타문자 + : 1회 이상
print(re.findall(r'[0-9]+',ss)) # 문자 집합 []
print(re.findall(r'[^0-9]+',ss)) # 문자 집합 [^] -> 부정
print(re.findall(r'\d+',ss)) # 특수문자 \d:숫자만 \D:문자만
print(re.findall(r'\D+',ss))
print(re.findall(r'[0-9]{2}',ss))
print(re.findall(r'[0-9]{2,3}',ss))
print(re.findall(r'[가-힝,a-z,A-Z]+',ss))
print(re.findall(r'^1234',ss)) # 문자열 시작
print(re.findall(r'만세$',ss)) # 문자열 끝

print()
ss = '''
<a href="abc1.html">abc1</a>
<a href="abc2.html">abc2</a>
<a href="abc3.html">abc3</a>
'''

print(ss)
result = re.findall(r'href="(.*)"',ss) # 작은 따옴표 안에 큰따옴표 슬수 있음, 큰 따옴표안에 작은 따옴표 쓸 수 있음
print(result) 

print()
p = re.compile('the', re.IGNORECASE) #flag 사용하기
print(p.findall('The dog the dog'))

s = """ My name is tom
I am happy"""
print(s)
p = re.compile('^.+',re.MULTILINE) #flag 사용하기
print(p.findall(s))
