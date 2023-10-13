# 추상클래스 : 추상 메소드를 한개 라도 가지고 있다면 추상 클래스가 된다.
from abc import abstractmethod, ABCMeta

class AbstracClass(metaclass = ABCMeta): # 추상 클래스 - 객체 생성 불가
    @abstractmethod
    def abcMethod(self): # 추상 메소드
        pass
    
    def normalMethod(self):
        print('추상 클래스 내의 일반 메소드')
        
# parent = AbstracClass() 
# TypeError: Can't instantiate abstract class AbstracClass with abstract method abcMethod => 인스턴스할 수 없음

'''
class Child1(AbstracClass):
    pass

c1 = Child1()  TypeError: Can't instantiate abstract class Child1 with abstract method abcMethod => 추상메소드 오버라이딩해야함
'''
        
class Child1(AbstracClass):
    name = '난 Child1'
    
    def abcMethod(self):
        print('Child1에서 추상 메소드를 오버라이딩 함 : 순전히 강요 때문')
        
   
        
c1 = Child1()
print(c1.name)
c1.abcMethod()
c1.normalMethod()

print('------------------------------------------------------------')

class Child2(AbstracClass):
    
    def abcMethod(self): # 오버라이딩 강제
        print('Child2에서 추상 메소드를 재정의함')
        print('추상의 마법에서 벗어남')
        
    def normalMethod(self): # 오버라이딩 선택
        print('추상클래스의 일반메소드 재정의')
        
c2 = Child2()
c2.abcMethod()
c2.normalMethod()


print('------다형성------------------------------------------')
good = c1
good.abcMethod()
good.normalMethod() 
print()     
good = c2
good.abcMethod()
good.normalMethod()  