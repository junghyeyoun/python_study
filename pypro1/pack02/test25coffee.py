'''
내가 처음 한 방법
class Machine:
    def ShowData(self,  cupCount,change):
        if change < 0:
            print("요금이 부족합니다.")
        else: 
            print(f"커피 {cupCount}잔과 잔돈 {change}원") 
        
        
class CoinIn:
    def __init__(self, cupCount, coin):
        self.cupCount = cupCount
        self.coin = coin

    def culc(self):
        change = self.coin - self.cupCount * 200
        return change

coin = int(input("동전을 입력하세요: "))
cupCount = int(input("몇 잔을 원하세요: "))

mc = Machine()
a = CoinIn(cupCount, coin)
change =  a.culc()
mc.ShowData(cupCount,change)
'''

class CoinIn:
    def culc(self, cupCount, coin):
        change = coin - cupCount * 200
        return change

class Machine:
    def __init__(self):
        self.coinIn = CoinIn()  # 클래스의 포함

    def showData(self):
        coin = int(input("동전을 입력하세요: "))
        cupCount = int(input("몇 잔을 원하세요: "))

        # CoinIn 클래스의 culc 메서드를 호출하여 잔돈 계산
        change = self.coinIn.culc(cupCount, coin)

        if change < 0:
            print("요금이 부족합니다.")
        else:
            print(f"커피 {cupCount}잔과 잔돈 {change}원")

if __name__ == '__main__':
    machine = Machine()
    machine.showData()  



