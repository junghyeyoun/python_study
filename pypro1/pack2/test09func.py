# 함수 : 반복소스의 단순화를 목표로, 여러개의 수행문을 하나의 이름으로 묶은 실행단위
# 내장함수

print(sum([3,4,5]))
print(bin(8))
print(int(1.5), float(3), str(5) + '오')
print(round(1.3), round(1.6)) # 반올림

import math # 일부의 기본으로 지원하지 않는 내장함수는 import
print(math.ceil(1.3), math.ceil(1.6)) # 올림
print(math.floor(1.3), math.floor(1.6)) # 버림

x = [10,20,30]
y = ['a','b']
for i in zip(x,y): # 쌍을 만들어줌
    print(i)
# 이외에도 여러개의 내장함수 있음

print('-----------------------------------------------------------------')

# 사용자 정의 함수
'''
def 함수명(parameter, ...):
    ...
    [return <반환값>] -> 주지 않아도 괜찮음
'''
def func1():
    print('func1 수행')


func1()
print(func1) # 그냥 func1만 쓰면 안됨
print('딴짓하다가')
func1()
imsi = func1() 
print(imsi) # None

    
def func2(para1,para2):
    result = para1 + para2
    aa = func3(result)
    if result%2 ==1:
        return aa
    else:
        return  result

def func3(result):
    if result % 2 ==1:
        return 
    else:
        return result

print(func2(3,4)) # None
print(func2(3,5))
print(func2, id(func2)) # 2531498186272

print()

def swap(a, b):
    # return (b, a)  리턴값 한개(집합으로 넘어 옴)
    return b, a

def func4():
    print('func4 처리')
    def func5():
        print('내부 함수 처리')
    func5()
    
func4()

# if 조건식안에  함수 사용 
def isodd(para):
    return para % 2 == 1
mydict = {x:x*x for x in range(11) if isodd(x)}
print(mydict)   