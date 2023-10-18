# multi processing을 통한 웹 스크래핑
import requests
from bs4 import BeautifulSoup as bs
import time 
from multiprocessing import Pool

# 스크래핑 대상 컨텐츠 : https://beomi.github.io/beomi.github.io_old/ 

def get_links():
    data = requests.get('https://beomi.github.io/beomi.github.io_old/').text # => str
    soup = bs(data,'html.parser')
    print(type(soup)) # <class 'bs4.BeautifulSoup'>
    my_titles = soup.select('h3 > a')
    data = []
    
    for title in my_titles:
        data.append(title.get('href'))
    return data

def get_content(link):
    abs_link = 'https://beomi.github.io' + link
    # print(abs_link)
    data = requests.get(abs_link).text
    print(data)  
    # soup = bs(data, 'html.parser') 
    # print(soup.select('h1')[0].text) # 제목만 찍기
    
if __name__ == '__main__':
    # print(get_links())
    # print(len(get_links()))
    start_time = time.time()
    
    '''
    # 직렬
    for link in get_links():
        get_content(link)
    '''
    
    # 병렬
    pool = Pool(processes = 4)
    pool.map(get_content, get_links()) 
    
    print('---%s 초 ---'%(time.time() - start_time)) 
    # 직렬 : 11.14298677444458 초
    # 병렬 : 4.604816675186157 초
    


