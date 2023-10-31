# 배열 연산
import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64) # 형변환
y = np.arange(5,9).reshape((2,2))
y = y.astype(np.float32) # 형변환
print(x,x.dtype)
print(y,y.dtype)

print(x+y) # -, *, /
print(np.add(x,y)) # substract, multiply, divide

# 참고 : 연산 속도
big_arr = np.random.rand(1000000)
print(big_arr)
%timeit sum(big_arr) # python 함수

%timeit np.sum(big_arr) # numpy 함수 : python이 더 빠름

# 벡터 연산 (내적)
v = np.array([9,10])
w = np.array([11,12])
print(v*w)
print(v.dot(w))
print(np.dot(v,w))
print(x.dot(v))
print(x.dot(y))
 
# numpy는 연산을 위한 함수 제공
print(np.sum(x)) # 모든 요소 합
print(np.sum(x, axis=0)) # 열에 대한 합
print(np.sum(x, axis=1)) # 행에 대한 합
print(np.mean(x))
print(np.argmax(x))
print(np.sqrt(x))

import numpy as np

names = np.array(['tom', 'james', 'tom', 'oscar'])
names2 = np.array(['tom', 'page', 'john'])

# 중복 제거
print(np.unique(names))

# names와 names2 배열 간에 중복된 요소를 찾기 위해 intersect1d를 사용
print(np.intersect1d(names, names2))

print(np.union1d(names, names2))

print(np.cumsum(x))

# 전치(transpose)
print(x)
print(x.T)

# Briadcasting : 크기가 다른 배열 간의 연산 시, 작은 배열은 큰 배열에 크기에 맞춰져 연산한다. 열이나 행이 더 많은 배열이 있을 경우 작은배열은 열과 행을 복제한다.
x = np.arange(1,10).reshape(3,3)
print(x)
y = np.array([1,0,1])
print(y)
z = np.empty_like(x)
print(z)

print()
for i in range(3):
  z[i] = x[i]+y
print(z)

print()
kbs = x+y # Broadcasting 연산 처리가 됨
print(kbs)

print('배열 자료를 파일 i/o')
print(x)
np.savetxt('my.txt',x)
print()
my2 = np.loadtxt('my.txt')
print(my2)