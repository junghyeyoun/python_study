# Thread 클래스 생속

import threading, time, sys

class MyThread(threading.Thread):
    def run(self):
        for i in range(1, 11):
            print('id={}-->{}'.format(threading.current_thread().name, i))
            time.sleep(0.2)
            
ths = []
for i in range(2):
    th = MyThread()
    th.start()
    ths.append(th)
    
for t in ths:
    t.join()
    
print('exit')