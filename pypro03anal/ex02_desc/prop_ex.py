# 비율 검정 : 집단의 비율이 어떤 특정한 값과 같은지를 검정

# one-sample
# A회사에서는 100명 중에 45명이 흡연을 한다. 국가 통계에서는 35%로 알려져 있다고 할 때, 두 그룹 간 비율이 동일한가?
# 귀무 : A회사의 흡연율과 국민 흡연율의 비율은 같다.
# 대립 : A회사의 흡연율과 국민 흡연율의 비율은 다르다.

import numpy as np 
from statsmodels.stats.proportion import proportions_ztest 

count = np.array([45])
nobs = np.array([100])
val = 0.35
z, p = proportions_ztest(count=count, nobs=nobs, value=val)
print(z)
print(p) # 0.04442318 < 0.05 귀무가설 기각. 따라서 A회사의 흡연율과 국민 흡연율의 비율은 다르다.

print()
# two-sample
# A회사 직원들 300명 중 100명이 햄버거를 먹었고, B회사 직원들 400명 중 170명이 햄버거를 먹었다고 할 때,
# 비율의 동질 여부를 검정해보자.
# 귀무 : A회사와 B회사의 햄버거 취식 비율은 같다.
# 대립 : A회사와 B회사의 햄버거 취식 비율은 다르다.
count = np.array([100, 170])
nobs = np.array([300, 400])

z, p = proportions_ztest(count=count, nobs=nobs, value=0) # 비율이 제시되지 않았을 때 value=0
print(z)
print(p) # 0.013675721698622408 < 0.05 귀무가설 기각. 따라서 A회사와 B회사의 햄버거 취식 비율은 다르다.