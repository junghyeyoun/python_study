# closure : scope에 제약을 받지 않는 변수들을 포함하고 있는 코드 블럭이다.
# 함수 내에서 선언한 지역변수를 함수 밖에서 사용하기 위한 방법
from sympy.physics.units import amount
from sympy.physics.units.definitions.dimension_definitions import amount_of_substance

def functimes(a,b):
    c = a*b
    print(c)
    return c

functimes(2, 3)
# print(c) # NameError : name 'c' is not defined

imsi = functimes(2, 3)
print(imsi)

print('closure test : 클로저를 사용하지 않은 경우 -------------------------------------------')
def out():
    count = 0
    def inn():
        nonlocal count # nonlocal 쓰면 밑에 오류 없어짐
        count +=1 # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
        return count
    print(inn())


out()
# print(out + 1) # TypeError: unsupported operand type(s) for +: 'function' and 'int'

print()
def outer():
    count = 0
    def inner():
        nonlocal count # nonlocal 쓰면 밑에 오류 없어짐
        count +=1 # UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
        return count
    return inner # <= 요게 클로저 : 내부 함수의 주소를 반환
    
var1 = outer() # <function outer.<locals>.inner at 0x0000017B2208DB20>
print(var1) # 출력 안됨
print(var1()) # 부를때마다 늘어남
print(var1())
print(var1())

var2 = outer()  
print(var2()) # var1()과 다름
print(var2())
print(id(var1), ' ',id(var2)) # 2070454000416   2070454001536 주소 다름

print('-- 수량*단가*세금(분기별로 동적)을 출력하는 함수 작성')
def outer2(tax):  # tax : 지역변수
    def inner2(su,dan):
        amount = su*dan*tax
        return amount
    return inner2

# 1분기에는 tax : 0.1
q1 = outer2(0.1)
print(q1) # <function outer2.<locals>.inner2 at 0x00000269B1859760>
result1 = q1(5,50000)
print(' result1 : ',result1)
result2 = q1(2,10000)
print(' result2 : ',result2)
print()

# 2분기
q2 = outer2(0.05)
result3 = q2(5,50000)
print(' result3 : ',result3)
result4 = q2(2,10000)
print(' result4 : ',result4)
print()