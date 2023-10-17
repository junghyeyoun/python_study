# process 실행
from subprocess import *

# Popen('calc.exe') # 응용 프로그램(계산기) 실행
# call('calc.exe') # 위와 같음
# print('계속')
# print('종료')

# Thread(light weight process라고도 함) 처리 => 동시에 여러개의 작업을 하는 것 처럼 할 수 있다.
# 시작, 실행, 종료의 세 단계로 구성됨
import threading, time

def run(id):
    for i in range(1,11):
        print('id={}--->{}'.format(id, i))
        time.sleep(0.5) # 비활성화 : sleep, wait / 활성화: ,notify

# 사용자 정의 thread를 사용하지 않은 경우 : 순차적으로 실행됨        
# run(1)
# run(2)

# 사용자 정의 thread를 사용한 경우 : 비순차적으로 실행됨  
th1 = threading.Thread(target=run, args=('일'))
th2 = threading.Thread(target=run, args=('이'))
th1.start()
th2.start()

th1.join() # 해당 스레드가 진행 되는 동안 메인 스레드는 대기 요청 =>  main thread는 제일 마지막에 실행
th2.join()

# 프로세스내에서 스레드가 실행되기 때문에 스레드가 끝나야 프로세스가 종료되고 프로그램이 끝나게 됨
print('프로그램 종료(메인 모듈은 자동으로 지원된 메인 스레드에 의해 실행)')