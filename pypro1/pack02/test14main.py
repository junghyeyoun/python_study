# 사용자 정의 모듈 call
print('뭔가를 하다가... 다른 모듈 호출')

import pack02.test14other

print('score : ',pack02.test14other.score)
print(pack02.test14other.__file__) # 경로명
print(pack02.test14other.__name__) # 모듈명

list1 = [1,2]
list2=[3,4]
pack02.test14other.listHap(list1,list2)

def abc():
    if __name__ == '__main__':
        print('메인 모듈이야')
abc()

print()
pack02.test14other.kbs()
from pack02.test14other import kbs, Mbc, score
kbs()
Mbc()
print(score)

# 다른 패키지 내의 모듈 읽기
import module_test.test14etc
module_test.test14etc.Hap(5, 3)

from module_test.test14etc2 import Gop   
Gop(5, 3) 

import test14etc2
test14etc2.Nanugi(5, 3) 
from test14etc2 import Nanugi
Nanugi(5, 3) 