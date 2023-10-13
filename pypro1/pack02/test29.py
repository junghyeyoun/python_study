# 다중 상속
class Tiger:
    data = '호랑이 세상'
    
    def cry(self):
        print('호랑이가 소리를 ...')
        
    def eat(self):
        print('맹수는 고기를 무척 좋아함')
        
class Lion:
    data = '호랑이 세상'
    
    def cry(self):
        print('사자의 울부짖음')
        
    def hobby(self):
        print('백수의 왕은 채팅을 즐김')
        
class Liger1(Tiger, Lion): # 다중 상속
    pass

obj1 = Liger1()
obj1.cry() # Tiger의 cry 실행
obj1.eat()
obj1.hobby()
print(obj1.data)

print('-----------------------------------------')
class Liger2(Tiger, Lion):
    data = '라이거 만세'
    
    def play(self):
        print('Liger2의 고유메소드')
        
    def hobby(self):
        print('라이거는 운동을 좋아함')
        
    def showHobby(self):
        self.hobby()
        super().hobby()
        print(self.data + ", "+super().data)
        
obj2 = Liger2()
obj2.cry()
obj2.showHobby()