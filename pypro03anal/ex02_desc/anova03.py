# 일원분산분석 검정
# 어느 음식점의 매출데이터와 날씨데이터 두 개의 파일을 이용해 최고 온도에 따른 음식점 매출액 평균의 차이를 검정
# 귀무 : 온도에 따른 음식점 매출액 평균의 차이가 없다.
# 대립 : 온도에 따른 음식점 매출액 평균의 차이가 있다.

import numpy as np 
import pandas as pd 
import scipy.stats as stats
import matplotlib.pyplot as plt 

# 매출 데이터
sales_data = pd.read_csv('../testdata/tsales.csv', dtype={'YMD':'object'})
print(sales_data.head(3))   # YMD -> 20190514
print(sales_data.info())

# 날씨 데이터
wt_data = pd.read_csv('../testdata/tweather.csv')
# print(wt_data.head(3))  # tm -> 2018-06-01 : 공통칼럼인 날짜 형태가 달라서 맞춰줘야함
print(wt_data.info())
wt_data.tm = wt_data.tm.map(lambda x:x.replace('-',''))
print(wt_data.head(3))

# merge
frame = sales_data.merge(wt_data, how='left',left_on='YMD',right_on='tm')
print(frame.head(3))
print(frame.tail(3),frame.shape)
print(frame.columns)

data = frame.iloc[:, [0,1,7,8]]
print(data.head(3)) # YMD(날짜)   AMT(매출액)   maxTa(최고기온)   sumRn(강수량)
print(data.isnull().sum()) # null 없음
print(data.maxTa.describe())
# plt.boxplot(data.maxTa)
# plt.show()

# 온도를 임의로 추움, 보통, 더움 (0,1,2) 세 구간으로 나눠 그룹을 형성
data['Ta_gubun'] = pd.cut(data.maxTa, bins=[-5, 8, 24, 37], labels=[0,1,2])
print(data.head(3))

print(data.corr()) # 상관관계 분석 :  상관계수로 관계 확인

# 세 그룹으로 데이터 분리 : 등분산성, 정규성 만족 여부 확인 - 종속변수가 해당
x1 = np.array(data[data.Ta_gubun==0].AMT)
x2 = np.array(data[data.Ta_gubun==1].AMT)
x3 = np.array(data[data.Ta_gubun==2].AMT)
print(x1[:10], len(x1))
print(x2[:10])
print(x3[:10])

print('\n 등분산성 확인')
print(stats.levene(x1,x2,x3).pvalue) # 0.039002396565063324 < 0.05 -> 등분산성 만족 x

print('\n 정규성 확인')
print(stats.ks_2samp(x1,x2).pvalue,stats.ks_2samp(x1,x3).pvalue,stats.ks_2samp(x2,x3).pvalue) # 정규성 만족 x

print('/n 온도별 매출액 평균')
tempAmt = data.loc[:, ['AMT','Ta_gubun']]
print(tempAmt.groupby('Ta_gubun').mean())
print(pd.pivot_table(tempAmt, index=['Ta_gubun'],  aggfunc='mean')) # 위와 같은 결과

tempAmtArr = np.array(tempAmt) # 배열로 바꿈
# print(tempAmtArr)

group1 = tempAmtArr[tempAmtArr[:,1]==0, 0]
group2 = tempAmtArr[tempAmtArr[:,1]==1, 0]
group3 = tempAmtArr[tempAmtArr[:,1]==2, 0]

# plt.boxplot([group1,group2, group3], showmeans=True, meanline=True)
# plt.show()
print('\n----one-way anova------------------------------------')
print()
print(stats.f_oneway(group1,group2, group3))
# pvalue -> 2.360737101089604e-34 < 0.05이므로 귀무가설 기각, 우연히 발생된거 아니라고 볼 수 있음
# 따라서 온도에 따른 음식점 매출액 평균의 차이가 있다.

print('정규성을 만족하지 않았으므로 kruskal-walis test')
print(stats.kruskal(group1, group2, group3)) 

print('정규성을 만족하지 않았으므로 welchi-anova test')
# pip install pingouin
from pingouin import welch_anova 
print(welch_anova(data=data, dv='AMT', between='Ta_gubun')) # pip install pingouin

print('\n사후검정')
from statsmodels.stats.multicomp import pairwise_tukeyhsd
postHoc = pairwise_tukeyhsd(tempAmt['AMT'], tempAmt['Ta_gubun'], alpha=0.05)
print(postHoc)

postHoc.plot_simultaneous()
plt.show()

