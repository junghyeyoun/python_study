# 공분산은 두 개 이상의 확률변수에 대한 관계를 알려주는 값이나, 값의 범위가 정해져 있지 않아 기준값을 설정할 수 없다.
# 이런 공분산의 문제를 해결하기 위해 공분산을 표준화한 상관계수를 사용한다. -1 ~ 1  사이이다.
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
plt.rc('font', family='malgun gothic')

data = pd.read_csv("../testdata/drinking_water.csv")
print(data.head(3), data.shape)  # 264행 3열 / 친밀도 적절성 만족도

# 표준편차
print(np.std(data.친밀도)) # 0.9685
print(np.std(data.적절성)) # 0.8580
print(np.std(data.만족도)) # 0.8271

plt.hist([np.std(data.친밀도),np.std(data.적절성),np.std(data.만족도)])
plt.show()

# 공분산
# print(np.cov(data.친밀도, data.적절성, data.만족도)) # 에러 : 확률변수 두개여야 함
print(np.cov(data.친밀도, data.적절성))
print(np.cov(data.친밀도, data.만족도))
print(data.cov()) # pandas

print()
# 상관계수
print(np.corrcoef(data.친밀도, data.적절성))
print(data.corr()) # pandas
print(data.corr(method='pearson'))  # 변수가 등간, 비율 척도. 정규분포
print(data.corr(method='spearman')) # 서열척도. 비정규분포
print(data.corr(method='kendall'))  # spearman과 유사

print()
# 만족도에 대한 다른 특성과 상관관계 확인
co_re = data.corr()
print(co_re['만족도'].sort_values(ascending=False))

# 시각화
data.plot(kind='scatter', x='만족도', y='적절성') # 산포도
plt.show()

from pandas.plotting import scatter_matrix 
attr = ['친밀도','적절성','만족도']
scatter_matrix(data[attr], figsize=(10,6)) # 산점도와 히스토그램 출력
plt.show()

# heatmap
import seaborn as sns 
sns.heatmap(data.corr()) # 색깔이 옅을수록 상관관계가 강함
plt.show()

# heatmap에 텍스트 표시 추가사항 적용해 보기
corr = data.corr()
# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool_)  # 상관계수값 표시
mask[np.triu_indices_from(mask)] = True
# Draw the heatmap with the mask and correct aspect ratio
vmax = np.abs(corr.values[~mask]).max()
fig, ax = plt.subplots()     # Set up the matplotlib figure

sns.heatmap(corr, mask=mask, vmin=-vmax, vmax=vmax, square=True, linecolor="lightgray", linewidths=1, ax=ax)

for i in range(len(corr)):
    ax.text(i + 0.5, len(corr) - (i + 0.5), corr.columns[i], ha="center", va="center", rotation=45)
    for j in range(i + 1, len(corr)):
        s = "{:.3f}".format(corr.values[i, j])
        ax.text(j + 0.5, len(corr) - (i + 0.5), s, ha="center", va="center")
ax.axis("off")
plt.show()