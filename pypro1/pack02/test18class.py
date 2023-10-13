# 모듈의 멤버 중 클래스
# 클래스는 새로운 이름 공간을 지원하는 단위로 메소드와 변수라는 멤버를 지닌다.
# 클래스는 이름 공간과 클래스가 생성하는 인스턴스 이름공간을 각각 갖는다.

class TestClass: # header이며 이하 소스는 body영역이 된다.
    aa = 1                  # 멤버변수는 클래스내에서 전역
    
    def __init__(self): # 생성자 / 메소드의 첫 파라미터는 self
        print('생성자')
        
    def __del__(self):
        print('소멸자')
        
    def printMsg(self): # 멤버 메소드
        name='한국인'  # 지역변수
        print(name)
        # print(aa) # 클래스내의 변수가 아니기 때문에 안됨
        print(self.aa) # 이렇게 써야함
        
test = TestClass() # 생성자 호출 후 인스턴스가 만들어짐 / test는 객체 변수(object variable)
print(test.aa)
# method call
test.printMsg() # 방법 1 : Bound method call
TestClass.printMsg(test) # 방법 2 : UnBound method call
print()
print(isinstance(test,TestClass)) # True
print(type(1))
print(type(test)) # <class '__main__.TestClass'>
print(id(test),id(TestClass)) # 2448977265424 2448978433424

del test # 인스턴스 삭제
