# 메소드 오버라이드
class Parent:
    def printData(self):
        pass
    
class Child1(Parent):
    def printData(self):
        print('Child1에서 오버라이드')
        
class Child2(Parent):
    def printData(self):
        print('Child2에서 오버라이딩 처리')
        print('부모 메소드의 이름은 같으나 기능이 다르다')
        
    def my(self):
        print('Child2 만의 고유 메소드')

c1 = Child1()
c1.printData()
print()
c2 = Child2()
c2.printData()
c2.my()

print('--------다형성')
par = Parent()
par = c1
par.printData()
print()
par= c2
par.printData()
print('-------------------------')
mbc = c1
mbc.printData()
mbc = c2
mbc.printData()
mbc.my()
print('-------------------------')
plist = [c1,c2]
for i in plist:
    i.printData()
    print()