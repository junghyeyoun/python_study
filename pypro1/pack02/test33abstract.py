# 추상
# 파이썬은 인터페이스 없음

from abc import ABCMeta, abstractmethod

class Friend(metaclass = ABCMeta):
    def __init__(self, name):
        self.name = name
     
    @abstractmethod   
    def hobby(self): 
        pass
        
    def printName(self):
        print('이름은 '+self.name)
        
class John(Friend):
    def __init__(self, name, addr):
        Friend.__init__(self, name)
        self.addr = addr
        
    def hobby(self): # 오버라이딩
        print(self.addr+' 거리를 산책함')
        
    def printAddr(self):
        print('주소는 '+self.addr)
        
class Chris(Friend):
    def __init__(self, name, addr):
        super().__init__(name)
        self.addr = addr
        
    def hobby(self):
        print(self.addr + '동네를 어슬렁 거림')
        print(self.addr +'에 오래전부터 살고 있음')
        
john =John('미스터존','역삼1동')
john.printName()
john.printAddr()
john.hobby()

print()
chris = Chris('크리스님','역삼2동')
chris.printName()
chris.hobby()

print('-----------------')
fri = john
fri.hobby()
print()
fri = chris
fri.hobby()