# python은 일급객체를 지원하는 일급함수를 사용
# 일급함수 : 함수안에 함수 선언 가능, 인자로 함수 전달, 반환값이 함수인 경우
from astropy.io.tests.mixin_columns import su

def func1(a,b):
    return a+b

func2 = func1
print(func1(3,4))
print(func2(3,4))

print()
def myFunc(func): # 인자로 함수
    def func4(): # 함수 안에 함수 선언
        print('난 내부 함수')
    func4()
    return func # 반환값이 함수

mbc = myFunc(func1) #인자로 함수
print(mbc(3,4))

print('축약함수(Lamda : 이름이 없는 한 줄 짜리 함수)')
# lamda 인자,,, :표현식
# def를 사용해야 할 정도로 함수의 내용이 복잡하지 않거나, def를 사용할 수 없는 상황일 때 람다를 적용

def hap(x,y):
    return x+y
print(hap(1,2))

print((lambda x, y:x+y)(1,2))

jtbc = lambda x, y:x*y
print(jtbc) # <function <lambda> at 0x0000020C7E05DB20>
print(jtbc(3,4))

mbc = lambda:print('단순한 람다')
mbc()

# 람다도 가변인수 가능
kbs = lambda a, su=10:a+su
print(kbs(5))

sbs = lambda a, *tu, **di:print(1,tu,di)
sbs(1,2,3,x=4,y=5)

# 리스트에 복수 람다를 저장
li = [lambda a,b:a +b,lambda a,b:a*b]
print(li[0](3,4))
print(li[1](3,4))

# 함수 내에 멤버로 람다 사용
# filter(조건 함수, 순회 가능한 데이터)
# filter() 함수는 두 번째 인자로 넘어온 데이터 중에서 첫 번재 인자로 넘어온 조건 함수를 만족하는 데이터만 찾아서 반환
print(list(filter(lambda a:a<5, range(10)))) # 0~10까지의 숫자중 5미만인 값만 출력
print(list(filter(lambda a:a%2, range(10))))  # 0~10까지의 숫자중 홀수인 값만 출력

# Q1) 1~100 사이의 정수 중 5의 배수이거나 7의 배수만 걸러 보기
print(list(filter(lambda a:a%5==0 or a%7==0 , range(1,101))))

# function decorator
print('함수 장식자 :  @함수명 -- meta 기능을 갖음')
# 장식자는 다른 함수를 감싼 함수다. 주 함수가 호출되면 그 반환 값이 장식자에게 건네진다.
# 그러면 장식자는 포함된 함수로 교체하여 함수를 반환한다.

def make2(fn):
    return lambda : "안녕" + fn()

def make1(fn):
    return lambda : "반가워" + fn()

def hello():
    return "한국인"

hi = make2(make1(hello)) # 안녕반가워한국인
print(hi())

# 위를 장식자로 표현

@make2
@make1
def hello2():
    return "신기해"

print(hello2())

print('재귀 함수(recursive function) : 함수가 자기자신을 호출 -- 반복처리에 사용' )
def countDown(su):
    if su == 0:
        print('완료')
        
    else:
        print(su, end = '  ')
        countDown(su-1) # 재귀
        
countDown(5)

print('1~10 까지의 정수의 합')
def funcHap(n):
    if n == 1:
        print('탈출')
        return True
    return n + funcHap(n-1)

result = funcHap(10)
print('10 까지의 정수의 합 : ',result)

print('계승(factorial) 처리를 위한 함수')
def myFact(a):
    if a ==1: return 1
    print(a)
    return a * myFact(a-1)

print('5!은 ',myFact(5))


