# singleton pattern

class SingletonClass:
    inst = None
    
    def __new__(cls):  # 객체의 생성을 담당. init method에 의해 초기화됨
        if cls.inst is None:
            cls.inst = object.__new__(cls)
        return cls.inst
    
    def aa(self):
        print('난 메소드야')
        
class SubClass(SingletonClass):
    pass

s1 = SubClass()
s2 = SubClass()
print(id(s1),id(s2)) # 1920192070032 1920192070032 => 같은 주소 (싱글톤 클래스를 상속받았기 때문에)

print()
s1.aa()
s2.aa()

print('\n------------------------------------------')
# 클래스의 멤버 변수를 고정

class Ani:
    __slots__ = ['irum','nai']
    
    def printData(self):
        print(self.irum, self.nai)
        
a = Ani()
a.irum = '호랑이' 
a.nai = 3
# a.eat = '치킨' # AttributeError: 'Ani' object has no attribute 'eat' => __slots__을 통해 변수를 고정시켰기 때문에 변수를 추가할 수 없음
a.printData()
        