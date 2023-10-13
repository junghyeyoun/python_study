# 다중 상속 연습
# https://cafe.daum.net/flowlife/RUrO/24 => 문제 링크 3번

class Animal:
    def move(self):
        pass

class Dog(Animal):
    name = '자쿰이'
    
    def move(self):
        print('자쿰이는 미용 안함')
       
class Cat(Animal):
    name = '수피아'
    
    def move(self):
        print('수피아는 집에서 미용함 가끔 가출함') 
        print('밤에 눈빛이 빛남')
        
class Wolf(Dog, Cat): # 다중 상속
    pass

class Fox(Cat, Dog): # 다중 상속
    def move(self):
        print('난 여우')
        
    def foxMethod(self):
        print('여우 고유 메소드')    
        
dog = Dog()
print(dog.name)
dog.move()

print()
cat = Cat()
print(cat.name)
cat.move()

print('---------------------------------------------')
wolf = Wolf()
print(wolf.name)# Dog을 먼저 적었기 때문에 Dog의 name
wolf.move() # Dog을 먼저 적었기 때문에 Dog의 move()를 받음

print()
fox = Fox()
print(fox.name) # Cat을 먼저 적었기 때문에 Cat의 name
fox.move() # 오버라이딩했기때문에 Fox의 move를 찍음
fox.foxMethod()
print(Wolf.__mro__)
# (<class '__main__.Wolf'>, <class '__main__.Dog'>, <class '__main__.Cat'>, <class '__main__.Animal'>, <class 'object'>) => 클래스 탐색 순서
print(Fox.__mro__)

print('-----다형성------------------------------------------')
sbs = wolf
sbs.move()

print()
sbs = fox
sbs.move()

print('--------------------')
animals = (dog,cat,wolf,fox)
for a in animals:
    a.move()
    print()


