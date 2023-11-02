
#자전거 공유 시스템 분석용
#: kaggle 사이트의 Bike Sharing in Washington D.C. Dataset를 편의상 조금 변경한 dataset을 사용함

#columns : 
#'datetime', 
#'season'(사계절:1,2,3,4), 
#'holiday'(공휴일(1)과 평일(0)), 
#'workingday'(근무일(1)과 비근무일(0)), 
#'weather'(4종류:Clear(1), Mist(2), Snow or Rain(3), Heavy Rain(4)), 
#'temp'(섭씨온도), 'atemp'(체감온도), 
#'humidity'(습도), 'windspeed'(풍속), 
#'casual'(비회원 대여량), 'registered'(회원 대여량), 
#'count'(총대여량)

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
plt.rc('font',family='malgun gothic')
plt.rcParams['axes.unicode_minus'] =False
import seaborn as sns

plt.style.use('ggplot') # R의 ggplot 스타일을 사용

# train dataset으로 탐색적 데이터분석 (EDA)
train = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/data/train.csv',parse_dates=['datetime'])
print(train.columns, ' ',train.shape,' ',train.dtypes)
print(train.head(2))
print(train.isnull().sum())
print(train.isna().sum())

# 참고 : null이 포함된 칼럼 확인용 시각화 라이브러리 pip install missingno를 사용한다.
print(train['datetime'].head(2)) # 연도별 월별 일별 시간별 대여량을 시각화하기 위해 연원일시분초열을 추가
train['year'] = train['datetime'].dt.year
train['month'] = train['datetime'].dt.month
train['day'] = train['datetime'].dt.day
train['hour'] = train['datetime'].dt.hour
train['minute'] = train['datetime'].dt.minute
train['second'] = train['datetime'].dt.second
# (10886, 12)
print(train.columns)
pd.set_option('display.max_columns',500)
print(train.head(2))

figure, (ax1,ax2,ax3,ax4) = plt.subplots(nrows=1,ncols=4) # 1행4열로 옆으로 나란히
figure.set_size_inches(15,5)

sns.barplot(data=train, x='year', y='count', ax=ax1)
sns.barplot(data=train, x='month', y='count', ax=ax2)
sns.barplot(data=train, x='day', y='count', ax=ax3)
sns.barplot(data=train, x='hour', y='count', ax=ax4)
ax1.set(ylabel='Count',title='연도별 대여량')
ax2.set(ylabel='month',title='월별 대여량')
ax3.set(ylabel='day',title='일별 대여량')
ax4.set(ylabel='hour',title='시간별 대여량')
plt.show()

# boxplot
fig, axes = plt.subplots(nrows=2,ncols=2) # 2행 2열
fig.set_size_inches(12,10)

sns.boxplot(data=train, y='count', orient='v', ax=axes[0][0])
sns.boxplot(data=train, x='season' ,y='count', orient='v', ax=axes[0][1])
sns.boxplot(data=train, x='hour' , y='count', orient='v', ax=axes[1][0])
sns.boxplot(data=train, x='workingday' , y='count', orient='v', ax=axes[1][1])
axes[0][0].set(ylabel='Count',title='대여량')
axes[0][1].set(xlabel='season' ,ylabel='Count',title='계절별 대여량')
axes[1][0].set(xlabel='hour', ylabel='Count',title='시간별 대여량')
axes[1][1].set(xlabel='workingday', ylabel='Count',title='근무일여부에 따른 대여량')
plt.show()


