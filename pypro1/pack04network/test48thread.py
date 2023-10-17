# thread를 이용해 날짜 및 시가 출력
import time

now = time.localtime()
# print(now)
print('오늘은 {0}년 {1}월 {2}일 {3}요일'.format(now.tm_year, now.tm_mon, now.tm_mday,now.tm_wday)) # 월요일은 0 ~ 일요일은 7
print('현재 {0}시 {1}분 {2}초'.format(now.tm_hour, now.tm_min, now.tm_sec))

print('-----------------------------')

import threading

def calender_show():
    now = time.localtime()
    print('오늘은 {0}년 {1}월 {2}일 {3}요일'.format(now.tm_year, now.tm_mon, now.tm_mday,now.tm_wday)) # 월요일은 0 ~ 일요일은 7
    print('현재 {0}시 {1}분 {2}초'.format(now.tm_hour, now.tm_min, now.tm_sec))
    
def myRun():
    while True:
        now2 = time.localtime()
        if now2.tm_min == 48:break
        calender_show()
        time.sleep(1)
    
        
# th = threading.Thread(target=calender_show)
th = threading.Thread(target=myRun)
th.start()

th.join()
print('프로그램 종료')