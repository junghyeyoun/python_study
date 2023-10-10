# 조건 판단문 if

var = 3
if var >= 5:
    print('크구나')  # 들여쓰기로 구분
    print('참')
else:
    print('거짓')

print('end')

money = 10000
age = 23

if money >= 500:
    item = 'apple'
    if age <=30:
        msg='어리네'
    else:
        msg = '먹었네'
else:
    item = '망고'
    if age >=20:
        ms='성인'
    else:
        msg = '아이'
        
print(item, msg)
print('end2')

jumsu = 85
if jumsu >= 90:
    print('우수')
elif jumsu >= 70: # else if = elif
    print('보통')
else:
    print('저조')
    
print()
jum = int(input('점수 입력:')) # int(), str() 형변환 함수
print(jum,type(jum))
if 90 <= jum <= 100:
    grade = '우수'
elif 70 <= jum < 90:
    grade = '보통'
else:
    grade = 'ㅜㅜ'

# print('결과' + jum) # TypeError: '<=' not supported between instances of 'int' and 'str'
print('결과 ' + str(jum)+'점은 ' +grade)

print()
names = ['홍길동','김치국','신기해']
if '홍길동' in names:
    print('내 친구야')
else:
    print('누구니?')

print()
a = 'kbs'
result = (5+4) if a == 'kbs' else 11 # 참이면 앞에 있는 거 거짓이면 뒤에 있는거
print(result)

a = 11
result2 = 'mbc' if a == 9 else 'kbs' 
print(result2)

a = 3
if a<5:
    print(0)
elif a<10:
    print(1)
else:
    print(2)
    
print(0 if a<5 else 1 if a<10 else 2)

result3 = a*2 if a>5 else a+2
print(result3)