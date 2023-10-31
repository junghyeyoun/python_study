# 수식을 통해 결과를 얻을 수 있으나 외부 모듈을 사용하면 수식없이 빠르게 결과를 얻을 수 있다.
# 개념을 이해하고 함수나 메소드를 활용하자
# 평균, 분산, 표준 편차 구하기

grades = [1,3,-2,4]

def grades_sum(grades):
    tot = 0
    for g in grades:
        tot += g
    return tot

def grades_avg(grades):
    tot = grades_sum(grades)
    ave = tot/len(grades)
    return ave

def grades_variance(grades):
    ave = grades_avg(grades)
    vari = 0
    for su in grades:
        vari += (su - ave)**2
    return vari / len(grades) # 모집단으로 계산

# return vari / (len(grades)-1) # 표본집단으로 계산
def grades_std(grades):
    return grades_variance(grades) **0.5

print('합은 ',grades_sum(grades))
print('평균은 ',grades_avg(grades))
print('분산은 ',grades_variance(grades))
print('표준편차는 ',grades_std(grades))
print()

import numpy as np
# numpy 사용
print('합은 ',np.sum(grades))
print('평균은 ',np.mean(grades),' ',np.average(grades))
print('분산은 ',np.var(grades))
print('표준편차는 ',np.std(grades))

# numpy 모듈 (라이브러리)
# 다차원 배열 자료구조인 ndarray, 선형대수 계산, 벡터 연산, 미적분 등을 지원
import numpy as np
ss = ['tom','oscar','john',12,12.3 ]
print(ss,type(ss))
ss2 = np.array(ss) # list를 ndarray로 변환, 같은  type으로 요소값 구성. 상위 type으로 변환 int -> float -> complex -> str
print(ss2,type(ss2))

# 메모리 비교(list vs ndarray)
# list
li = list(range(1, 10))
print(li)
print(id(li[0]), id(li[1]))

a = np.array([1.,2,3]) # 1차원 배열
print(a, type(a), a.dtype, a.shape, a.size) # 1뒤에 . 찍어서 float 됨
print(a[0],a[2])
a[0] = 7 # 인덱싱 가능
print(a)

b = np.array([[1,2,3],[4,5,6]], dtype='float32') # 2차원 배열 - 2행 3열
print(b, type(b), b.dtype, b.shape, b.size)
print(b[0,0],b[0,2]) # 1 3 -> 스칼라
print(b[[0]]) # [[1 2 3]] -> 차원 유지

c = np.zeros((2,2))
print(c)

d = np.ones((2,2))
print(d)

e = np.full((2,2), 7)
print(e)

f = np.eye(3) # 기본값 float / 주대각은 1이고 나머지는 0인 전방행렬 만들어줌
print(f)

np.random.seed(0) # 난수 고정
print(np.random.rand(5)) # 균등분포를 따르는 난수
print(np.random.randn(5)) # 정규분포를 따르는 난수

print(np.random.randint(10, size=6)) # 0이상 10이하의 정수 6개
print(np.random.randint(10, size=(3,4)))
print(np.random.randint(10, size=(3,4,5)))

# 인덱싱, 슬라이싱
a = np.array([1,2,3,4,5])
print(a)
print(a[0])
print(a[1:3])
print(a[1:5])

print()
b = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(b)
print(b[:]) # : => 모두다
print(b[0,0])
print(b[[0]],b[0],b[0][0]) # b[0] => 차원 축소 / b[[0]] => 차원 유지
print(b[1:, 0:2])

print()
c = b[:2, 1:3] # sub array
print(c)
print(c[0,0])
c[0,0] =99
print(c)
print(b)
print(li * 10)
for i in li:
    print(i * 10, end=' ')

print('\n')
# nbarray
num_arr = np.array(li)
print(id(num_arr[0]), id(num_arr[1]))
print(num_arr * 10)