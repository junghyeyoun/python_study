import numpy as np 
import scipy.stats as stats
import pandas as pd 

# [one-sample t 검정 : 문제1]  
# 영사기에 사용되는 구형 백열전구의 수명은 250시간이라고 알려졌다. 
# 한국연구소에서 수명이 50시간 더 긴 새로운 백열전구를 개발하였다고 발표하였다. 
# 연구소의 발표결과가 맞는지 새로 개발된 백열전구를 임의로 수집하여 수명시간 관련 자료를 얻었다. 
# 한국연구소의 발표가 맞는지 새로운 백열전구의 수명을 분석하라.
#   305 280 296 313 287 240 259 266 318 280 325 295 315 278

# 귀무 : 영사기에 사용되는 구형 백열전구의 수명은 300시간이다.
# 대립 : 영사기에 사용되는 구형 백열전구의 수명은 300시간이 아니다.

one_sample = [305, 280, 296, 313, 287, 240, 259, 266, 318, 280, 325, 295, 315, 278]
print(np.array(one_sample).mean()) # 289.7857142857143

print('\n 정규성 확인 : ',stats.shapiro(one_sample)) # pvalue -> 0.8208622932434082 > 0.05 정규성 만족
result1 = stats.ttest_1samp(one_sample, popmean=300)
print(result1)
print('statistic(t값) : %.5f, pvalue:%.5f'%result1)
# 해석 : pvalue:0.14361 > 0.05이므로 귀무가설 채택. 영사기에 사용되는 구형 백열전구의 수명은 300시간이다.

print('\n\n-----------------------------------------------------')
# [one-sample t 검정 : 문제2] 
# 국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간으로 파악되었다. A회사에서 생산된 노트북 평균시간과 차이가 있는지를 검정하기 위해서 A회사 노트북 150대를 랜덤하게 선정하여 검정을 실시한다.
# 실습 파일 : one_sample.csv
# 참고 : time에 공백을 제거할 땐 ***.time.replace("     ", "")

# 귀무 : 국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간이다.
# 대립 : 국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2 시간이 아니다.
data1 = pd.read_csv('../testdata/one_sample.csv')
print(data1)
data1['time'] = data1['time'].str.replace(" ", "")
data1 = data1[data1['time'] != ''] 

data1['time'] = data1['time'].astype('float')

result2 = stats.ttest_1samp(data1.time, popmean=5.2 )
print(result2)
print('statistic(t값) : %.5f, pvalue:%.5f'%result2)

# 해석 : pvalue: 0.00014 < 0.05이므로 귀무가설 기각. 국내에서 생산된 대다수의 노트북 평균 사용 시간이 5.2이 아니다.

print('\n\n-----------------------------------------------------')
# [one-sample t 검정 : 문제3] 
# https://www.price.go.kr/tprice/portal/main/main.do 에서 
# 메뉴 중  가격동향 -> 개인서비스요금 -> 조회유형:지역별, 품목:미용 자료(엑셀)를 파일로 받아 미용 요금을 얻도록 하자. 
# 정부에서는 전국 평균 미용 요금이 15000원이라고 발표하였다. 이 발표가 맞는지 검정하시오.

# 귀무 : 전국 평균 미용 요금이 15000원이다.
# 대립 : 전국 평균 미용 요금이 15000원이 아니다.

data2 = pd.read_csv('../testdata/beauty.csv', encoding='euc-kr')
print(data2)
data2 = data2.dropna(axis=1)
data2 = data2.drop(['번호', '품목'], axis=1)
print(np.mean(data2.T.iloc[:,0])) # 18311.875
print(data2)

result3 = stats.ttest_1samp(data2.iloc[0], popmean=15000 )
print(result3)
print('statistic(t값) : %.5f, pvalue:%.5f'%result3)
# 해석 : pvalue: 0.00001 < 0.05이므로 귀무가설 기각. 전국 평균 미용 요금이 15000원이 아니다.