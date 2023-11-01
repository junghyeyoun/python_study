# Selenium 툴을 이용해 브라우저를 통제. 웹 크롤링 가능
import time
from selenium import webdriver

'''
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get('https://daum.net')
browser.quit()\
'''

#크롬 드라이버 실행 후 검색 하기 
'''
browser = webdriver.Chrome()  #Optional argument, if not specified will search path.
browser.get('http://www.google.com/xhtml');
search_box = browser.find_element("name", "q")
search_box.send_keys('파이썬')
search_box.submit()
time.sleep(5)          # Let the user actually see something!
browser.quit()
'''

#  이클립스 또는 jupyter notebook 등의 편집기에서 실행해 보기 

try:
    url = "https://www.daum.net"
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.get(url);
    browser.save_screenshot("daum_img.png")
    browser.quit()
    print('성공')
except Exception:
    print('에러')

    