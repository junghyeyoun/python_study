# class : 멤버로 변수와 메소드를 포함한 집합체. 객체 중심의 독립적인 프로그래밍이 가능함. OOP 구현 가능.

class Car:
    handle = 0
    speed = 0
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        
    def showData(self):
        km = '킬로미터'
        msg = '속도 :  '  +str(self.speed) +km
        return msg
    
print(Car.handle)
# Car.showData() -> TypeError: Car.showData() missing 1 required positional argument: 'self'

car1 = Car('tom',80)
print('car1 : ',car1.handle, car1.name, car1.speed)
car1.color = '보라'  # 원형클래스는 모르지만 car1 객체에 color 변수 추가 / 메소드는 추가 안됨
print('car1 : ',car1.color) 
print()

car2 = Car('james',100)
print('car2 : ',car2.handle, car2.name, car2.speed)

print()
print(Car.handle, car1.handle, car2.handle) # 0 0 0
print(Car.speed, car1.speed, car2.speed) # 0 80 100
print(car1.color)
# print(car2.color) => err
# print(Car.color) => err
print(Car, car1, car2)
print(id(Car),id(car1),id(car2)) # 2055742768576 2055741670096 2055741670160 => 주소 다 다름
print(car1.__dict__) # 객체의 멤버 확인
print(car2.__dict__)

print('----메소드--------------------------')
print('car 1 : ',car1.showData())
print('car 2 : ',car2.showData())

car1.speed = 55
car2.speed = 88
print('car 1 : ',car1.showData())
print('car 2 : ',car2.showData())
print()

car1.handle = 1
print('car1 : ',car1.handle, car1.name, car1.speed) # car1 :  1 tom 55
print('car2 : ',car2.handle, car2.name, car2.speed) # car2 :  0 james 88

