from scipy import stats
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

# 추론 통계 분석 중 가설검정 : 독립표본 t-검정(independent tow-sample t-test)
# 비교 집단이 두개인 경우에 평균이 단순히 유의한 차이가 있는지를 검정하는 방법
# 예) 오리온 초코파이와 롯데 초코파이의 무게가 같은가?

# 서로 독립인 두 집단의 평균 차이 검정(independent tow-sample t-test)
# 남녀의 성적, A반과 B반의 키, 경기도와 충청도의 소득 따위의 서로 독립인 두 집단에서 얻은 표본을 독립표번(two sample)이라고 한다.

# 실습 1) 남녀 두 집단 간 파이썬 시험의 평균 차이 검정. 남녀의 시험 평균이 우연히 같은 확률은 얼마일까?

# 귀무 : 두 집단 간 파이썬 시험의 평균에 차이가 없다.
# 대립 : 두 집단 간 파이썬 시험의 평균에 차이가 있다.

male = [75,85, 100, 72.5, 86.5]
female = [63.2, 76, 52, 100, 70]
print(np.mean(male), np.mean(female))  # 83.8 72.24

# two_sample = stats.ttest_ind(male, female)
two_sample = stats.ttest_ind(male, female, equal_var=True, alternative='two-sided')
print(two_sample)   # TtestResult(statistic=1.233193127514512, pvalue=0.2525076844853278, df=8.0)
# 해석 : pvalue=0.252 > 0.05 이므로 귀무 채택 (통계적 유의성으로 표현)

# 참고 : Effect-size(효과 크기) - 두 집단 평균 차이를 물리적으로 세등급으로 분리(물리적)해 표현
# 효과 크기(Cohen's d) = 두 표본 집단의 평균 차이 / 추정된 표준편차
imsi = male + female
print(imsi) 
print((np.mean(male) - np.mean(female)) / np.std(imsi))  # 0.799이므로 효과크기가 커서 두 그룹의 평균에 차이가 크다고 할 수 있다.

print('/n-----------------------------------------------------------')

# 실습 2) 두 가지 교육방법에 따른 평균시험 점수에 대한 검정 수행 two_ sample.csv
# 귀무 : 두 가지 교육방법에 따른 평균시험 점수에 차이가 없다.
# 귀무 : 두 가지 교육방법에 따른 평균시험 점수에 차이가 있다.
data = pd.read_csv('../testdata/two_sample.csv')
print(data.head(3), data.shape) # (50, 5)
# print(data.isnull().sum()) # score 두개가 null -> 제거 또는 특정값으로 대체 가능

ms = data[['method','score']]
print(ms.head(2))
print(ms['method'].unique()) # [1 2]

# 교육방법별 데이터 추출
m1 = ms[ms['method']==1]
m2 = ms[ms['method']==2]
print(m1.head(2))
print(m2.head(2))

# 교육방법에서 점수 추출
score1 = m1['score'] 
score2 = m2['score']
print(score1.isnull().sum()) # 0
print(score2.isnull().sum()) # 2 -> 제거, 0 또는 평균으로 대체 가능
# score2 = score2.fillna(0)
score1 = score1.fillna(score1.mean()) # -> na 없지만 확인하지 않고 대체해도 됨
score2 = score2.fillna(score2.mean())

print('\n정규성 확인') 
import seaborn as sns 
'''
sns.histplot(score1, kde=True, color='r')
sns.histplot(score2, kde=True, color='b')
plt.show()
'''

print(stats.shapiro(score1).pvalue) # 0.36798644065856934 > 0.05이므로 정규성 만족
print(stats.shapiro(score2).pvalue) # 0.6714232563972473 > 0.05이므로 정규성 만족

print('\n등분산성 확인') 
print(stats.levene(score1, score2).pvalue) # 모수 검정일 때 # 0.4568427112977609 > 0.05
print(stats.fligner(score1, score2).pvalue) # 모수 # 0.44323735267062647 > 0.05
print(stats.bartlett(score1, score2).pvalue) # 비모수 검정일 때  # 0.26789717886602216 > 0.05
# levene 가장 많이 씀 세 값 다 0.05보다 크므로 등분상성을 만족한다.

result = stats.ttest_ind(score1, score2)
print('\nt-value : %.5f, p-value : %.5f'%result) # t-value : -0.19649, p-value : 0.84505
print(np.mean(score1), np.mean(score2)) # 5.199999999999999 5.246666666666667
# 판정 : p-value -> 0.84505 > 0.05 귀무가설 채택. 따라서, 두 가지 교육방법에 따른 평균시험 점수에 차이가 없다.

print('\n등분산성을 만족한 경우 : ',stats.ttest_ind(score1, score2).pvalue)
print('등분산성을 만족한 경우 : ',stats.ttest_ind(score1, score2, equal_var=True).pvalue)
print('등분산성을 만족하지 못한 경우 : ',stats.ttest_ind(score1, score2, equal_var=False).pvalue)
# 등분산성을 만족하지 못한 경우 welchi test 가능
print()
print('정규성을 만족할 경우 : ',stats.ttest_ind(score1,score2).pvalue)
# print('정규성을 만족하지 못한 경우 : ',stats.wilcoxon(score1,score2).pvalue) # 두 집단의 크기가 같은 경우
print('정규성을 만족하지 못한 경우 : ',stats.mannwhitneyu(score1,score2).pvalue) # 두 집단의 크기가 다른 경우

# 방법상의 차이가 있고 값도 조금씩 달라지지만 가설을 뒤집을 만큼의 차이가 나진 않음


