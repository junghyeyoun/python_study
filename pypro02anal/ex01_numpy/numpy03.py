# 배열에 행 또는 열 추가, 삭제
import numpy as np

aa = np.eye(3)
print(aa)

# 열 추가
bb = np.c_[aa, aa[2]]
print(bb)

# 행 추가
cc = np.r_[aa,[aa[2]]]
print(cc)

print('열 삽입을 이용해 행을 열로 변환 가능')
a = np.array([1,2,3])
print(np.c_[a])
print(a.reshape((3,1)))

print(a)
b = np.append(a,[4,5]) # 열 추가
print(b)
c = np.insert(a, 0, [6,7]) # 열 삽입
print(c)
d = np.delete(a,1)
print(d)

aa = np.arange(1,10).reshape(3,3)
print(aa)
print(np.insert(aa,1,99)) # 차원 축소
print(np.insert(aa,1,99, axis=1)) # 행 기준
print(np.insert(aa,1,99, axis=0)) #

bb = np.arange(10,19).reshape(3,3)
print(bb)
cc = np.append(aa,bb)
print(cc)

cc = np.append(aa,bb,axis=0)
print(cc)

cc = np.append(aa,bb,axis=1)
print(cc)

# 조건 연산 : where(조건, 참, 거짓)
x = np.array([1,2,3])
y = np.array([4,5,6])
conditionData = np.array([True, False, True])
result = np.where(conditionData, x, y)
print(result)

aa = np.where(x >= 2)
print(aa, x[aa])
print(np.where(x>=2,'T','F'))
print(np.where(x>=2,x,x+100))
print()
print(bb)
print(np.where(bb > 0, 10, bb))

aa = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])

print(aa)
print(np.delete(aa, 1))  # axis를 지정하지 않아서 1차원 배열로 축소됨
print(np.delete(aa, 1, axis=0))  # axis=0을 지정하여 행을 삭제
print(np.delete(aa, 1, axis=1))  # axis=1을 지정하여 열을 삭제


print(x)
print(y)
mbc = np.concatenate([x,y]) # 배열 집합
print(mbc)

x1,x2 = np.split(mbc,2)
print(x1)
print(x2)

a = np.arange(1,17).reshape(4,4)
print(a)
x1,x2 = np.hsplit(a,2)
print(x1)
print(x2)

x1,x2 = np.vsplit(a,2)
print(x1)
print(x2)

# sampling : 표본 추출
li = np.array([1,2,3,4,5,6,7])

# 복원 추출
for _ in range(5):
    print(li[np.random.randint(0, len(li)-1)],end=' ')

# 비복원 추출
import random
print(random.sample(list(li), k=5))
print(random.sample(range(1,46), k=5))

print(list(np.random.choice(range(1,46),6)))
print(list(np.random.choice(range(1,46),6,replace=False))) # 비복원
print(list(np.random.choice(range(1,46),6,replace=True))) # 복원

# 가중치를 부여한 랜덤 추출
ar = 'air book cat desk e f god'
ar = ar.split(sep=' ')
print(ar)
print(np.random.choice(ar, 3, p=[0.1,0.1,0.1,0.1,0.1,0.1,0.4])) # god가 나올 확률 높아짐

