# 변수의 생존 범위 : global, local
# Local > Enclosing function > Global > Builtin

player = '국가대표'  # 전역변수 (모듈의 어디서든 공유 가능)

def funcSports():
    name = '신기루'  # 지역변수(함수 내에서만 유효)
    player = '지역대표'  # 지역변수에 우선순위가 있기 때문에 지역변수가 찍힘
    print(name, player)
    
funcSports()

print()
a = 1; b=2; c=3
print('출력 1 -- a:{}, b:{}, c:{}'.format(a,b,c))
def outerfunc():
    a = 4 # 출력 2,3에만 영향을 미침
    b = 5
    def innerfunc():
        global c # c가 전역변수가 됨
        nonlocal b  # 전역변수말고 outerfunc의 지역변수의 수준으로 올라감
        # c = 6  # 출력 2에만 영향을 미침
        print('출력2 -- a:{}, b:{}, c:{}' .format(a,b,c))
        c = 6 # UnboundLocalError: cannot access local variable 'c' where it is not associated with a value
        b = 7 # 위와 같은 오류남 (b를 전역변수로 바꾸기 전까지는)
    innerfunc()
    print('출력3 -- a:{}, b:{}, c:{}' .format(a,b,c))
    
outerfunc()
print('출력4 -- a:{}, b:{}, c:{}' .format(a,b,c))

print('인수 키워드 매칭 ----------------------')
def ShowGugu(start=1, end=5):
    for dan in range(start, end +1):
        print(str(dan) + '단 출력', end=" ")
    print()

ShowGugu(2,3) # 위치 매개변수
ShowGugu() #초기치
ShowGugu(2) # 기본값 매개변수/start=2
ShowGugu(start=2, end=3)
ShowGugu(end=3, start=2) # 키워드매개변수/반대로 줘도 됨 
ShowGugu(2, end=4)
# ShowGugu(start=2, 4) # SyntaxError: positional argument follows keyword argument
# ShowGugu(end=3, 2) # 위와 같은 오류

# 가변 매개변수 : 인수의 개수가 동적임
*a, b = [1,2,3,4,5]
def fu1(*ar):
    print(ar)
    for a in ar:
        print('밥 : '+a)
fu1('공기밥' ,'주먹밥')
fu1('공기밥','주먹밥','김밥')

def fu2(bap,*ar):
# def fu2(*ar, bap): # error
    print(bap)
    print(ar)
    for a in ar:
        print('밥 : '+a)
fu2('공기밥' ,'주먹밥')
fu2('공기밥','주먹밥','김밥')

print()
def selectCalc(choice, *ar):
    if choice == '+' :
        imsi = 0
        for i in ar:
            imsi += i
    elif choice == '*' :
        imsi = 1
        for i in ar:
            imsi *= i
    return imsi

print(selectCalc('+',1,2,3,4,5)) # tuple 자료
print(selectCalc('*',1,2,3,4,5))

# dict를 인수로 전달
def fu3(w, h, **etc): # ** dict로 처리 (값 벨류 형식으로)
    print('몸무게:{},키:{}'.format(w,h))
    print(etc)

fu3(66, 177,  irum='홍길동')
fu3(66, 177,  irum='고길동', nai=22)

print()
def fuFinal(a,b,*c,**d):
    print(a,' ',b)
    print(c)
    print(d)
    
fuFinal(1,2)
fuFinal(1,2,3,4,5)
fuFinal(1,2,3,4,5,m=6,n=7)
