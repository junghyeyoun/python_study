# 사용자 정의 모듈 call
print('뭔가를 하다가... 다른 모듈 호출')

# 같은 패키지 내의 모듈 읽기
import pack2.test14other

print('score : ',pack2.test14other.score)
print(pack2.test14other.__file__) # 경로명 /__는 시스템이 가지고 있는 것
print(pack2.test14other.__name__) # 모듈명

list1 = [1,2]
list2 = [3,4]
pack2.test14other.listHap(list1,list2)

def abc():
    if __name__ == '__main__':
        print('메인 모듈이야 라고 외치다')
abc()

print()
pack2.test14other.kbs()
from pack2.test14other import kbs, Mbc, score # from과 import의 순서는 상관 x
kbs()
Mbc()
print(score)

# 다른 패키지 내의 모듈 읽기 - 같은 패키지내에서 읽던지, 다른 패키지내에서 읽던지 방법 같음 (자바와 다른점)  프로젝트가 달라지면 안됨
import module_test.test14etc
module_test.test14etc.Hap(5, 3)

# Lib이나 다른 PYTHONPATH에 있는 폴더에 모듈을 추가하고서 쓸 수 있음
from module_test.test14etc import Cha
Cha(5,3)

import test14etc2
test14etc2.Gop(5, 3)
from test14etc2 import  Nanugi
Nanugi(5,3)
