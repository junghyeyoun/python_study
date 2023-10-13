# class 멤버 호출 관련 

kor = 100

def abc():
    print('모듈의 멤버 함수')

class MyClass:
    kor = 90
    
    def abc(self):
        print('abc 메소드')
        
    def show(self):
        # kor = 80
        # print(self.kor) # 90
        print(kor) # 80 / kor = 80 주석처리하면 100 => 변수 호출 순서 : 지역변수 > 모듈 변수 
        self.abc() # method를 호출
        abc() # 함수를 호출
        
my = MyClass()
my.show()

from pack2.test20other import Our
print(Opack02
print()
print('our1 ---------')
our1 = Our()
print(our1.a)
print('our2 ---------')
our2 = Our()
our2.a =2
print(our2.a)

