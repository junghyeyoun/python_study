# [ANOVA 예제 1]
# 빵을 기름에 튀길 때 네 가지 기름의 종류에 따라 빵에 흡수된 기름의 양을 측정하였다.
# 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 존재하는지를 분산분석을 통해 알아보자.
# 조건 : NaN이 들어 있는 행은 해당 칼럼의 평균값으로 대체하여 사용한다.

# 귀무 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 있다.
# 대립 : 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 없다.
import numpy as np 
import pandas as pd 
import scipy.stats as stats
import matplotlib.pyplot as plt

data = {
    'kind': [1, 2, 3, 4, 2, 1, 3, 4, 2, 1, 2, 3, 4, 1, 2, 1, 1, 3, 4, 2],
    'quantity': [64, 72, 68, 77, 56, np.nan, 95, 78, 55, 91, 63, 49, 70, 80, 90, 33, 44, 55, 66, 77]
}

df = pd.DataFrame(data)
# NaN 있는 행 삭제
df['quantity'].fillna(df['quantity'].mean(), inplace=True)
# print(df)

# 네 그룹으로 분리 
o1 = np.array(df[df.kind == 1].quantity)
o2 = np.array(df[df.kind == 2].quantity)
o3 = np.array(df[df.kind == 3].quantity)
o4 = np.array(df[df.kind == 4].quantity)
print(o1, len(o1))
print(o2, len(o2))
print(o3, len(o3))
print(o4, len(o4))

print('\n 등분산성 확인')
print(stats.levene(o1,o2,o3,o4).pvalue) # 0.3268969935062273 > 0.05 -> 등분산성 만족 

print('\n 정규성 확인')
print(stats.shapiro(o1).pvalue) # 0.8680412769317627
print(stats.shapiro(o2).pvalue) # 0.5923926830291748
print(stats.shapiro(o3).pvalue) # 0.48601073026657104
print(stats.shapiro(o4).pvalue) # 0.4162167012691498
# 모두 정규성 만족

print('\n 기름별 흡수양 평균')
mean_quantity = df.groupby('kind')['quantity'].mean()
print(mean_quantity)

significance_level = 0.05  # 유의수준
f_value, p_value = stats.f_oneway(o1,o2,o3,o4)
print('pvalue : ',p_value)
if p_value > significance_level:
    print("귀무가설 채택, 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 없다.")
else:
    print("대립가설 채택, 기름의 종류에 따라 흡수하는 기름의 평균에 차이가 있다.")
# 귀무가설 채택, 귀무가설 기각 실패
    
print('\n 사후검정')
from statsmodels.stats.multicomp import pairwise_tukeyhsd
postHoc = pairwise_tukeyhsd(df['quantity'], df['kind'], alpha=0.05)
print(postHoc)

postHoc.plot_simultaneous()
plt.show()

print('***'*20)

# [ANOVA 예제 2]
# DB에 저장된 buser와 jikwon 테이블을 이용하여 총무부, 영업부, 전산부, 관리부 직원의 연봉의 평균에 차이가 있는지 검정하시오. 
# 만약에 연봉이 없는 직원이 있다면 작업에서 제외한다.

# 귀무 : 부서별 직원의 연봉의 평균에 차이가 없다.
# 대립 : 부서별 직원의 연봉의 평균에 차이가 있다.
import MySQLdb
import pickle
import sys

# 데이터 불러오기 
try:
    with open('mydb.dat', mode='rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('읽기 오류 : ',e)
    sys.exit()
    
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = '''
        select buser_name, jikwon_pay from jikwon right outer join buser
        on buser_num = buser_no
    '''
    cursor.execute(sql)
    data2 = pd.DataFrame(cursor.fetchall(), columns=['buser_name', 'jikwon_pay'])
    print(data2)
    
except Exception as e:
    print('처리 오류 : ',e)
finally:
    cursor.close()
    conn.close()
    
# 네그룹으로 분리
b1 = np.array(data2[data2.buser_name == '총무부'].jikwon_pay)
b2 = np.array(data2[data2.buser_name == '영업부'].jikwon_pay)
b3 = np.array(data2[data2.buser_name == '전산부'].jikwon_pay)
b4 = np.array(data2[data2.buser_name == '관리부'].jikwon_pay) 
print(b1, len(o1))
print(b2, len(o2))
print(b3, len(o3))
print(b4, len(o4))

print('\n 등분산성 확인')
print(stats.levene(b1,b2,b3,b4).pvalue) # 0.7980753526275928 > 0.05 -> 등분산성 만족 

print('\n 정규성 확인')
print(stats.ks_2samp(b1,b2).pvalue) # 0.3357 > 0.05 정규성 만족
print(stats.ks_2samp(b1,b3).pvalue) # 0.5751 > 0.05 정규성 만족
print(stats.ks_2samp(b1,b4).pvalue) # 0.5363 > 0.05 정규성 만족
print(stats.ks_2samp(b2,b3).pvalue) # 0.3357 > 0.05 정규성 만족
print(stats.ks_2samp(b2,b4).pvalue) # 0.6406 > 0.05 정규성 만족
print(stats.ks_2samp(b3,b4).pvalue) # 0.5363 > 0.05 정규성 만족

print('\n 부서별 연봉 평균')
mean_buser = data2.groupby('buser_name')['jikwon_pay'].mean()
print(mean_buser)

f_value, p_value = stats.f_oneway(b1,b2,b3,b4)
print('pvalue : ',p_value)
if p_value > significance_level:
    print("귀무가설 채택, 부서별 직원의 연봉의 평균에 차이가 없다.")
else:
    print("대립가설 채택, 부서별 직원의 연봉의 평균에 차이가 있다.")
# 귀무가설 채택, 귀무가설 기각 실패

print('\n 사후검정')
postHoc2 = pairwise_tukeyhsd(data2['jikwon_pay'], data2['buser_name'], alpha=0.05)
print(postHoc2)

postHoc2.plot_simultaneous()
plt.show()


