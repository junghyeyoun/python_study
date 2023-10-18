# 3번
from cryptography.x509 import name
import wheel
for i in range(1,100):
    if(i%3==0 or  i%4==0 and i%7!=0):
        print(i , end=' ')

# 6번
print()       
a =1.5; b=2; c=3;
def kbs():
    a=20
    b=30
    def mbc():
        global c
        nonlocal b
        print('a:{},b:{},c:{}'.format(a,b,c))
        c = 40
        b =50
        
    mbc()
kbs()

# 7번      
*v1, v2, v3 = {1,2,3,4,5,1,2,3,4,5}
print(v1)
print(v2)
print(v3)

# 8번
lambda m,n:m+n*5
print((lambda m,n:m+n*5)(3,2))

# 10번
'''
try:
    aa = int(input())
    if aa == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    bb = 10 / aa
    print("결과:", bb)
except ZeroDivisionError as e:
    print(e)

'''

# 11번
print()
i = 1
while i <= 10:
    j = 10
    disp = ' ' * i
    while j >= i:
        disp += '*'
        j -= 1
    print(disp)
    i += 1
#12번
'''
def Youn():
    year = int(input('연도 입력:'))
    if year%4==0 and year%100!=0 or year%400==0:
        print(year,'년은 윤년')
    else: 
        print(year,'년은 평년')
Youn()
'''
#13번
print('13번-----------')
i = 0
while True:
    if i % 10 != 3:
        i += 1
        continue
             
    if i > 100:
        break
               
    print(i, end=' ')
    i += 1


#14번
'''
import MySQLdb

import pickle
with open(r'mydb.dat',mode='rb') as obj:
    config = pickle.load(obj)
    
def jikwon():
    try:
        conn = MySQLdb.connect(**config)
        cursor = conn.cursor()
        
        jikwon_jik = input('직급 입력:')
        sql = """
        select jikwon_no, jikwon_name, jikwon_jik, buser_num from jikwon
        where jikwon_jik = '{0}'
        """.format(jikwon_jik)
        
        cursor.execute(sql)
        datas = cursor.fetchall()
        
        if len(datas) == 0:
            print(jikwon_jik+'직급은 없어요')
            return 
        
        for jikwon_no, jikwon_name, jikwon_jik, buser_num in datas:
            print(jikwon_no, jikwon_name, jikwon_jik, buser_num)
        
    except Exception as e:
        print('err : ',e)
    finally:
        cursor.close()
        conn.close()
        
if __name__ == '__main__':
    jikwon()
'''

print()
# 15번
class Bicycle:
    
    def __init__(self, name, wheel, price):
        self.name = name
        self.wheel = wheel
        self.price = price 
    
    def display(self):
        totprice = self.price * self.wheel
        print('{0}님 자전거 바퀴 가격 총액은 {1}입니다.'.format(self.name, totprice))

if __name__ == '__main__':
    gildong = Bicycle('길동', 2, 50000)      
    gildong.display()

