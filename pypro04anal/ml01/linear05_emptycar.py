# 단순 선형 회귀 : mtcars dataset, ols()
# 상관관계가 약한 경우와 강한 경우를 나눠 분석 모델을 작성 후 비교

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
import statsmodels.api
import numpy as np
plt.rc('font', family='malgun gothic')

# 과학적 추론 방식은 크게 두 가지로 분류
# 귀납법 : 개별사례를 수집해서 일반적인 법칙을 생성
# 연역법 : 사실이나 가정에 근거해 논리적 추론에 의해 결론을 도출

mtcars = statsmodels.api.datasets.get_rdataset('mtcars').data
print(mtcars.head(3), mtcars.shape)  # (32, 11)
print(mtcars.columns)
print(mtcars.describe())
print(mtcars.corr())
print(np.corrcoef(mtcars.hp, mtcars.mpg)[0,1])  # -0.776
print(np.corrcoef(mtcars.wt, mtcars.mpg)[0,1])  # -0.867

# 시각화
# plt.scatter(mtcars.hp, mtcars.mpg)
# plt.xlabel('마력수')
# plt.ylabel('연비')
# slope, intercept = np.polyfit(mtcars.hp, mtcars.mpg, 1)  # 기울기와 절편을 구함
# plt.plot(mtcars.hp, mtcars.hp * slope + intercept, color='r')  # 뒤에 수식은 예측값
# plt.show()

print('\n단순선형회귀')
result = smf.ols('mpg ~ hp', data = mtcars).fit()  # 학습을 하라 = fit
print(result.summary())  # 모델에 대한 유의수준 Prob (F-statistic) : 1.79e-07 < 0.05 유의한 모델이다, R-squared : 0.602 60% 정도의 설명력을 갖는다
print('마력수 : {}에 대한 연비 예측 결과 : {}'.format(110, -0.0682 * 110 + 30.0989))
print('마력수 : {}에 대한 연비 예측 결과 : {}'.format(110, result.predict(pd.DataFrame({'hp':[110]}))))

print('\n다중선형회귀')
result2 = smf.ols('mpg ~ hp+wt', data = mtcars).fit()  # 학습을 하라 = fit
print(result2.summary())  # 모델에 대한 유의수준 Prob (F-statistic) : 1.79e-07 < 0.05 유의한 모델이다, R-squared : 0.602 60% 정도의 설명력을 갖는다
print('마력수 : {}, 차체무게:{} 에 대한 연비 예측 결과 : {}'.format(110,5, result2.predict(pd.DataFrame({'hp':[110],'wt':[5]}))))
