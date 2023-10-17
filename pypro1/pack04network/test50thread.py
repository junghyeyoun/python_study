import threading

g_count = 0  # 전역 변수는 스레드 간에 공유됩니다.

lock = threading.Lock()

def threadCount(id, count):
    global g_count
    for i in range(count):
            lock.acquire(count) # 임의의 스레드가 공유자원 사용 시 다른 스레드는 대기 상태
            print('id %s ==> count : %s, g_count: %s' % (id, i, g_count))
            g_count = g_count + 1
            lock.release() # 대기상태 해제

threads = []

for i in range(1, 6):
    thread = threading.Thread(target=threadCount, args=(i, 5))  # "target=" 오탈자 수정
    threads.append(thread)
    thread.start()

# 모든 스레드의 종료를 대기합니다.
for thread in threads:
    thread.join()
print('최종 g_count:', g_count)
print('프로그램 종료')
