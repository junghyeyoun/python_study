# 공분산  / 상관계수 연습
import numpy as np 

# 공분산
print(np.cov(np.arange(1,6), np.arange(2,7)))   # 2.5
print(np.cov(np.arange(1,6), (3,3,3,3,3)))  # 0
print(np.cov(np.arange(1,6), np.arange(6,1,-1)))    #-2.5

print()
x = [8,3,6,6,9,4,3,9,4,3]
print('평균 : ', np.mean(x),' 분산 : ',np.var(x))

# y = [6,2,4,6,9,5,1,8,4,3]
y = [600,200,400,600,900,500,100,800,40,30]
print('평균 : ', np.mean(y),' 분산 : ',np.var(y))

import matplotlib.pyplot as plt 
plt.scatter(x, y)
plt.plot(x,y,'o')
plt.show()

# print('x,y의 공분산 : ',np.cov(x,y))
print('x,y의 공분산 : ',np.cov(x,y)[0,1])

# print('x,y의 상관계수 : ',np.corrcoef(x,y))
print('x,y의 상관계수 : ',np.corrcoef (x,y))

# 피어슨 상관 계수
# r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계 (이미지: P = -1)
# r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계(이미지: -1<p<0)
# r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계(이미지: -1<p<0)
# r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계(이미지: p=0)
# r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계(이미지: 0<p<1)
# r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계(이미지: 0<p<1)
# r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계 (이미지: P = 1)

print('--곡선의 경우에는 상관계수는 의미 없다.----------')
m = [-3, -2, -1, 0, 1, 2, 3]
n = [9, 4, 1, 0, 1, 4, 9]
plt.plot(m,n)
plt.show()
print('m, n의 공분산 : ', np.cov(m,n)[0,1])
print('m, n의 상관계수 : ', np.corrcoef(m,n)[0,1])