# 교촌 치킨 - 제목, 가격 / 제일싼거, 비싼거, 표준편차, 평균
import urllib.request as req
from bs4  import BeautifulSoup
import pandas as pd

url = 'https://www.kyochon.com/menu/chicken.asp'
kyochon = req.urlopen(url)
# print(kyochon.read())
soup = BeautifulSoup(kyochon,'html.parser')
# print(soup)
name = soup.select("#tabCont01 > ul > li > a > dl > dt")
price = soup.select("#tabCont01 > ul > li> a > p.money > strong")
# print(name)

'''
# 가격을 숫자 리스트로 변환 -> 리스트말고 데이터프레임형태로 해야 이름과 가격 동시에 저장할 수 있음 
prices = [int(p.string.replace(',', '')) for p in price]

for n, p in zip(name, prices):
    print(n.string,':',p,'원')
'''  
data = {'이름': [n.string for n in name], '가격': [int(p.string.replace(',', '')) for p in price]}
df = pd.DataFrame(data)

print(df)
print()

# 가격 리스트에서 제일 싼 가격과 비싼 치킨 찾기
min_price = min(df['가격'])
max_price = max(df['가격'])

cheapest_chicken = df[df['가격'] == min_price]['이름'].values[0]
most_expensive_chicken = df[df['가격'] == max_price]['이름'].values[0]

print('제일 싼 치킨:',cheapest_chicken,'-', min_price, '원')
print('제일 비싼 치킨:',most_expensive_chicken,'-', max_price, '원')

# 평균 가격 계산
average_price = df['가격'].mean()
print('평균 가격: ',round(average_price),'원')

# 표준편차 계산
std_deviation = df['가격'].std()
print('표준편차: ',round(std_deviation),'원')
