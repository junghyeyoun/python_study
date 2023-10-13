# 클래스의 포함 관계 : 자원의 재활용이 목적 (약결합)
# 완성차를 조립하기 위해 여러 개의 부품(여기서는 핸들로 한정)을 객체로 만들어 불러다 사용

from pack02.test22handle import PohamHandle

class PohamCar:
    turnShowMessage = '정지'
    
    def __init__(self, ownerName):
        self.ownerName = ownerName  # 할당 연산자로 수정
        self.handle = PohamHandle()
        
    def turnHandle(self, q):
        if q > 0:
            self.turnShowMessage = self.handle.rightTurn(q)
        elif q < 0:
            self.turnShowMessage = self.handle.leftTurn(q)
        elif q == 0:
            self.turnShowMessage = '직전'
            self.handle.quantity = 0
           
if __name__ == '__main__':
    tom = PohamCar('톰 아저씨')
    tom.turnHandle(20)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShowMessage + str(tom.handle.quantity))
    tom.turnHandle(0)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShowMessage + str(tom.handle.quantity))
    
    print()
    oscar = PohamCar('오스카 형')
    oscar.turnHandle(-10)
    print(oscar.ownerName + '의 회전량은 ' + oscar.turnShowMessage + str(oscar.handle.quantity))
    
   
