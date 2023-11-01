# 웹사이트 스크래핑 연습
import urllib.request as req
from bs4  import BeautifulSoup
import urllib

print('연습 1 : 위키백과에서 검색된 자료 읽기--------')
url = 'https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0'
wiki = req.urlopen(url)
# print(wiki.read())
soup = BeautifulSoup(wiki,'html.parser')
# print(soup)
print(soup.select("#mw-content-text > div.mw-parser-output > p"))
# mw-content-text > div.mw-parser-output > p  (selector copy)
print()
result = soup.select("div.mw-parser-output > p > b")
print(result)

for s in result:
    print(s.string)
    
print('연습 2 : daum에서 뉴스 자료 읽기--------')    
url='https://news.daum.net/society#1'   
daum = req.urlopen(url)
soup = BeautifulSoup(daum,'lxml')
print()
datas = soup.select('div.direct-link > a')
print(datas)
for i in datas:
    href=i.attrs['href']
    text =i.string
    print('href:%s, text:%s' %(href, text))
    
datas = soup.findAll('a')
for i in datas:
    href=i.attrs['href']
    text = i.string 
    print('href:%s,text:%s' %(href,text))

print('\n 연습 3: naver에서 시장지표 자료 중 미국 USD 자료 읽기(일정 시간 마다 주기적으로 읽어 파일로 저장)')
import  datetime
import time

def workingFunc():
    url = 'https://finance.naver.com/marketindex/'
    data = req.urlopen(url)
    soup=BeautifulSoup(data, 'lxml')
    price = soup.select_one("div.head_info > span.value").string
    print('미국 USD : ',price)
    t = datetime.datetime.now()
    fname = './usd/' + t.strftime('%Y-%m-%d-%H-%M-%S')+'.txt'
    
    with open(fname, mode='w') as f:
        f.write(price)
    
while True:
    workingFunc()
    time.sleep(3)