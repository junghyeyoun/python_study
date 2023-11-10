# 단순선형회귀 분석 모델 작성 : ols() 함수 사용 - OLS Regression Results 내용 알기
# 결정론적 선형회귀분석 방법 - 확률적 모형에 불확실이 덜하다.
from scipy import stats
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
plt.rc('font',family='malgun gothic')
import statsmodels.formula.api as smf

df = pd.read_csv('../testdata/drinking_water.csv')
print(df.head(3), df.shape)
print(df.corr(method='pearson')) 
# 독립변수(x, feature) : 적절성
# 종속변수(y, label) : 적절성
# 목적 : 주어진 feature와 결정적 기반에서 학습을 통해 최적의 회귀계수를 찾아내는 것
model = smf.ols(formula = '만족도 ~ 적절성',data=df).fit()
print(model.summary()) # 전체보기
# 부분적으로 보기
print(model.params)
print(model.pvalues)

# 예측값 
print(df.적절성[:5].values)
new_df = pd.DataFrame({'적절성':[4,3,4,2,2]})
new_pred = model.predict(new_df)
# 0.588 설명력이 있는 모델로 검정
print('만족도 실제 값 : ',df['만족도'][:5].values)
print('만족도 예측 값 : ',new_pred.values)

# 선형 회귀 모델의 결과를 나타내는 OLS(Ordinary Least Squares) 회귀 결과 표
# 1.   Dep. Variable (종속 변수): 만족도 (Dependent Variable)가 회귀 모델에서 종속 변수로 사용되었다는 것을 나타냅니다.
# 2.   Model: 회귀 모델의 종류를 나타냅니다. 여기서는 OLS (최소제곱법) 회귀 모델을 사용했습니다.
# 3.   Method:   회귀 분석에 사용된 메소드를 나타냅니다. 여기서는 Least Squares (최소제곱법)를 사용했습니다.
# 4.   Date:   회귀 분석이 수행된 날짜를 나타냅니다.
# 5.   Time:   회귀 분석이 수행된 시간을 나타냅니다.
# 6.   No. Observations:   사용된 샘플의 수 (관측치의 개수)입니다.
# 7.   Df Residuals:   잔차의 자유도, 모델에서 추정한 파라미터 수를 뺀 값입니다.
# 8.   Df Model:   모델의 자유도, 사용된 설명 변수의 수를 나타냅니다.
# 9.   Covariance Type:   공분산 유형을 나타냅니다. 여기서는 "nonrobust"로 나타내어 간단한 공분산 행렬이 사용되었습니다.
# 10.   coef (계수):   회귀 계수를 나타냅니다. "Intercept"는 절편을, "적절성"은 해당 설명 변수의 회귀 계수를 나타냅니다.
# 11.   std err (표준 오차):   회귀 계수의 표준 오차를 나타냅니다.
# 12.   t-statistic (t-통계량):   회귀 계수에 대한 t-통계량을 나타냅니다. t-통계량은 해당 계수가 0일 때의 표준 오차에 대한 비율을 나타냅니다.
# 13.   P>|t| (p-value):   각 계수에 대한 p-value를 나타냅니다. 이 값은 귀무가설이 해당 계수가 0인지에 대한 확률을 나타내며, 일반적으로 0.05보다 작으면 해당 계수는 통계적으로 유의미하다고 판단됩니다.
# 14.   [0.025 0.975]:   95% 신뢰구간 (Confidence Interval)을 나타냅니다. 이는 계수가 해당 구간 안에 있을 확률이 95%라는 것을 의미합니다.
# 15.   R-squared (결정 계수):   모델이 설명하는 변동의 비율을 나타냅니다. 1에 가까울수록 모델이 데이터를 잘 설명하고 있다는 것을 의미합니다.
# 16.   Adj. R-squared (조정된 결정 계수):   R-squared를 보정한 값으로, 모델에 추가된 설명 변수의 수에 대한 보정을 반영합니다.
# 17.   F-statistic (F-통계량):   모델 전체의 통계적 유의성을 나타내는 F-통계량입니다. 높을수록 모델이 통계적으로 유의미하다는 것을 의미합니다.
# 18.   Prob (F-statistic):   F-통계량에 대한 p-value를 나타냅니다. 이 값이 작으면 모델 전체가 통계적으로 유의미하다고 판단됩니다.
# 19.   Log-Likelihood (로그 우도):   최대 로그 우도를 나타냅니다. 로그 우도가 높을수록 모델이 데이터를 잘 설명하고 있다는 것을 의미합니다.
# 20.   AIC (Akaike Information Criterion):   모델의 상대적인 품질을 나타내는 지표 중 하나입니다. AIC가 낮을수록 모델이 더 적절하다고 판단됩니다.
# 21.   BIC (Bayesian Information Criterion):   AIC와 유사하게 모델의 상대적인 품질을 나타내는 지표 중 하나입니다.
# 22.   Omnibus:   잔차의 정규성을 검정하는데 사용되는 값입니다. - 모델 유의성 
# 23.   Prob(Omnibus):   Omnibus 검정에 대한 p-value를 나타냅니다. - 0.05보다 작으면 유의
# 24.   Durbin-Watson:   잔차의 자기상관을 검정하는데 사용되는 값입니다. - 잔차의 독립성
# 25.   Jarque-Bera (JB):   잔차의 정규성과 첨도에 대한 검정을 수행하는 값입니다. - 자기상관
# 26.   Prob(JB):   Jarque-Bera 검정에 대한 p-value를 나타냅니다. - 오차의 정규성 가정을 검정 0.05보다 작으면 유의
# 27.   Skew (왜도):   잔차의 왜도를 나타냅니다.
# 28.   Kurtosis (첨도):   잔차의 첨도를 나타냅니다.
# 29.   Cond. No. (Condition Number):   회귀 행렬의 조건 수를 나타냅니다. 이 값이 크면 다중공선성의 가능성이 있을 수 있습니다.


