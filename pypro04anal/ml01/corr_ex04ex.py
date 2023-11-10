# 상관관계 문제)
# Advertising.csv 파일을 읽어 tv,radio,newspaper 간의 상관관계를 파악하시오. 
# 그리고 이들의 관계를 heatmap 그래프로 표현하시오. 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
plt.rc('font', family='malgun gothic')

data = pd.read_csv("../testdata/Advertising.csv")
data = data.drop(['sales','no'], axis=1)
print(data.head(3), data.shape)
# 상관계수 표로 보기
print(data.corr()) 
# 두개씩 보기
print(np.corrcoef(data.tv, data.radio)) # 0.05480866 -> 다소 높은 상관관계
print(np.corrcoef(data.tv, data.newspaper)) #  0.05664787 -> 다소 높은 상관관계
print(np.corrcoef(data.radio, data.newspaper)) # 0.35410375 -> 낮은 상관관계

# heatmap
import seaborn as sns 
sns.heatmap(data.corr()) 
plt.show()