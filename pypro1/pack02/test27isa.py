# 상속 연습
print('클래스는 모듈의 멤버')

class Person:
    say = '사람이야'  # public
    nai = '20'
    __my = 'private  멤버'  # private =>  앞에 언더바 두번 + 변수명 / 현재 클래스내에서만 사용 가능
        
    def __init__(self, nai):
        print('Person 생성자')
        self.nai = nai
    
    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai, self.say))
        
    def hello(self):
        print('안녕')
        print(self.__my)
        
    @staticmethod
    def kbs(tel):
        print('kbs_static method(클래스 소속) : ',tel)
        
print(Person.say, Person.nai)
# Person.printInfo(self) => NameError: name 'self' is not defined
p = Person('25')
print(p.say, p.nai)
p.printInfo()
p.hello()

p.kbs("111-1234")
Person.kbs("111-1234") # 권장

print('***'*20)
class Employee(Person):
    subject ='근로자'
    
    def __init__(self):
        print('Employee 생성자')
        
    def printInfo(self):
        print('Employee의 오버라이딩된 printInfo')
        
    def eprintInfo(self):
        print(self.say, super().say)
        self.hello()
        self.printInfo()
        super().printInfo()
        
e = Employee()
print(e.say, e.subject)
e.eprintInfo()

print('***'*20)
class Worker(Person):
    say = 'worker의 say'
    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai)  # Bound method call
        
    def printInfo(self): # 오버라이딩
        print('Worker에 선언된 printInfo')
        
    def wprintInfo(self):
        self.printInfo()
        super().printInfo()

w = Worker('30')
print(w.say, w.nai)
w.wprintInfo()

print("^^^" *20)
class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        # super().__init__(nai) # Bound method call
        Worker.__init__(self, nai) # Unbound method call
        
    def pprintInfo(self):
        self.wprintInfo()
        
            
    def hello2(self):
        print('안녕')
        # print(self.__my) # __my는 Person의 private 멤버이기 때문에 error
        
pr = Programmer('33')
print(pr.say, pr.nai)
pr.pprintInfo()
pr.hello2() 
pr.kbs("111-1234")
Programmer.kbs("111-1234")

# 원형 클래스 4개와 각각의 클래스마다 인스턴스를 따로 만들어 인스턴스 총 8 개

print('클래스 타입 확인 ---')
print(type(1.2))
print(type(pr))
print(Programmer.__bases__) # (<class '__main__.Worker'>,) => 부모클래스 알려줌 / 다중상속이 가능하기 때문에 (,) 형태로 집합형임
print(Worker.__bases__) # (<class '__main__.Person'>,)
print(Person.__bases__)  # (<class 'object'>,)
        