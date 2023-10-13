# 클래스의 상속
class Animal:
    def __init__(self):
        print('Animal 생성자')
        
    def move(self):
        print('움직이는 생물')
        
class Dog(Animal):
    def __init__(self):
        print('댕댕이 생성자')
    
    def my(self):
        print('난 댕댕이')
        
dog1 = Dog()
dog1.my()
dog1.move()

# 자바와 차이점 
# 이름
    # Python: 클래스 생성자의 이름은 항상 __init__입니다. 클래스 내에 __init__ 메서드를 정의하여 초기화 로직을 구현합니다.
    # Java: 클래스 생성자의 이름은 클래스 이름과 동일합니다. Java에서는 생성자를 클래스 이름과 동일한 이름으로 정의합니다.
# 상속 및 부모 클래스 생성자 호출
    # Python: 하위 클래스 생성자에서 부모 클래스의 생성자를 직접 호출할 필요가 없습니다. Python은 자동으로 부모 클래스의 생성자를 호출합니다.
    # Java: 하위 클래스 생성자에서 명시적으로 super()를 사용하여 부모 클래스의 생성자를 호출해야 합니다.

print()
class Horse(Animal):
    pass

horse1 = Horse()
horse1.move()
