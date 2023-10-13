# 클래스의 포함관계 : 국인이네 냉장고(객체)에 음식(객체) 담기

class Fridge:
    isOpened = False # 냉장고 문 개폐 여부 확인용 변수
    foods = [] # 음식물 담기용 리스트
    
    def open(self):
        self.isOpened = True
        print('냉장고 문 열림')
        
    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing) # 포함관계
            print('냉장고 안에 음식 담기 완료')
            self.list()
        else:
            print('냉장고 문이 닫혀서 음식을 넣을 수 없음')
            
    def close(self):
        self.isOpened = False
        print('냉장고 문 닫힘')
        
    def list(self):
        for f in self.foods:
            print('-',f.name, f.expiry_date)
        print()
    
# 냉장고에 담길 음식물 클래스
class FoodData:
    def __init__(self,  name, expiry_date):
        self.name = name
        self.expiry_date = expiry_date
        
# 실행
fr = Fridge()
apple = FoodData('사과','2023-11-5')
fr.put(apple) # 냉장고 문이 닫혀서 음식을 넣을 수 없음

fr.open()
fr.put(apple)
fr.close()

print('------')
coke = FoodData('콜라','2025-10-5')
fr.open()
fr.put(coke)
fr.close()
        