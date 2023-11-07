# 추론 통계 분석 중 가설 검정 : 단일표본 t-검정(one-sample t-test)
# 정규분포의(모집단) 표본에 대해 기대값을 조사(평균의 차이 사용)하는 검정 방법
# 예) 새우깡 과자 무게가 진짜 120g이 맞는가?

# 실습1) 어느 남성 집단의 평균키 검정
# 귀무 : 남성의 평균키는 177.0이다.(모집단의 평균)
# 대립 : 남성의 평균기킄 177.0이 아니다.

import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

one_sample = [167.0, 182.7, 169.6, 176.8, 185.0]
'''
plt.boxplot(one_sample)
plt.xlabel('data')
plt.ylabel('height')
plt.grid()
plt.show()
'''
print(np.array(one_sample).mean())
print(np.array(one_sample).mean()-177.0)

print('\n 정규성 확인 : ',stats.shapiro(one_sample)) # pvalue=0.5400515 > 0.05 
result = stats.ttest_1samp(one_sample, popmean=177.0)
print(result)
print('statistic(t값) : %.5f, pvalue:%.5f'%result)
# 해석 : pvalue:0.83563 > 0.05이므로 귀무가설 채택. 수집된 자료는 우연히 발생된 것이라고 볼 수 있다.


print('\n\n-----------------------------------------------------')
# 실습 예제 2)
# A중학교 1학년 1반 학생들의 시험결과가 담긴 파일을 읽어 처리 (국어 점수 평균검정) student.csv
# 귀무 : 학생들의 국어 점수 평균은 80.0이다.
# 대립 : 학생들의 국어 점수 평균은 80.0이 아니다.

data = pd.read_csv('../testdata/student.csv')
print(data.head(3))
print(data.describe())
print(np.mean(data.국어)) # 72.9 / 80.0 

result2 = stats.ttest_1samp(data.국어, popmean=80.0 )
print(result2)
print('statistic(t값) : %.5f, pvalue:%.5f'%result2)
# 해석 : pvalue:0.19856 > 0.05이므로 귀무가설 채택. 학생들의 국어 점수 평균은 80.0이다. 현재 발생한 국어점수는 우연히 발생한 것이다.

print('\n\n-----------------------------------------------------')
# 실습 예제 3)
# 여아 신생아 몸무게의 평균 검정 수행 babyboom.csv
# 여아 신생아의 몸무게는 평균 2800(g)으로 알려져 왔으나 이보다 더 크다는 주장이 나왔다.
# 표본으로 여아 18명을 뽑아 체중을 측정하였다고 할 때 새로운 주장이 맞는지 검정해 보자.

# 귀무 : 여아 신생아의 몸무게는 평균 2800(g)이다.
# 대립 : 여아 신생아의 몸무게는 평균 2800(g)보다 크다.

data2 = pd.read_csv('../testdata/babyboom.csv')
print(data2.head(3), len(data2)) # 44
fdata = data2[data2['gender']==1]
print(fdata, len(fdata)) # 18
print(np.mean(fdata['weight'])) # 3132.4444444444443

# 정규성 확인
print(stats.shapiro(fdata.iloc[:2])) # pvalue=0.000176288565 < 0.05이므로 정규성 만족 못함

# 정규성 확인 시각화 1 : Q-Q plot
stats.probplot(fdata.iloc[:,2],plot=plt) 
plt.show()

# 정규성 확인 시각화 2 : histogram
sns.displot(fdata.iloc[:,2], kde=True)
plt.show()

result3 = stats.ttest_1samp(fdata.weight, popmean=2800 )
print(result3)
print('statistic(t값) : %.5f, pvalue:%.5f'%result3)




