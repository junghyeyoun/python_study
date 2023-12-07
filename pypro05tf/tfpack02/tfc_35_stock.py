# -*- coding: utf-8 -*-
"""tfc_35_stock.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tQbwvGR2fCTYkNApWaKCB3TfWxipia2y
"""

# CNN + LSTM + Dense 모델을 작성해 주가 예측
# 삼성전자 증권표준코드 05930
!pip install finance-datareader

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import FinanceDataReader as fdr
import warnings
warnings.filterwarnings('ignore')

STOCK_CODE = '005930'
stock = fdr.DataReader(STOCK_CODE)
print(stock.head(3))
print(stock.tail(3))

print('상관관계 : ',stock.corr())
stock.reset_index(inplace=True)
print(stock.head(3))
stock.drop(['Change'], axis='columns', inplace=True)

# Date열을 이용해 연도별 주가 변동 시각화
# Date열을 연,월,일로 분리해 새로운 열을 추가
stock.set_index('Date', inplace=True)

stock['year'] = stock.index.year
stock['month'] = stock.index.month
stock['day'] = stock.index.day

df = stock.loc[stock['year'] >= 2000]

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x=df.index, y='Close')
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Stock Price Variation Over Time')
plt.show()

time_step = [['2000','2005'],['2005','2010'],['2010','2015'],['2015','2023']]
fig, axes = plt.subplots(2,2)
fig.set_size_inches(8,4)
for i in range(4):
  ax = axes[i//2, i%2]
  df = stock.loc[((stock.index > time_step[i][0]) & (stock.index > time_step[i][1]))]
  sns.lineplot(y=df['Close'], x=df.index, ax=ax)
  plt.xlabel('Time')
  plt.ylabel('Price')
plt.tight_layout()
plt.show()

# 전처리
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scale_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
df_scaled = scaler.fit_transform(stock[scale_cols])
df = pd.DataFrame(df_scaled, columns=scale_cols)
print(df.head(3))

# train_test_split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(df.drop('Close',1),df['Close'], test_size=0.2, random_state=12, shuffle=False)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
print(x_train[:2])
print(y_train[:2])

# Dataset을 활용 sequence dataset 구분
import tensorflow as tf
def window_dadtaset_func(series, window_size, batch_size, shuffle):
  series = tf.expand_dims(series, axis=1)
  ds = tf.data.Dataset.from_tensor_slices(series) # ex) (60000, 28, 28) -> (28*28)의 크기 6만개로 슬라이싱
  ds = ds.window(window_size + 1, shift=1, drop_remainder=True) # Dataset.window(그룹화할 윈도우 크기, 이동수)
  ds = ds.flat_map(lambda w:w.batch(window_size+1))
  if shuffle:
    ds = ds.shuffle(buffer_size=1000)
  ds = ds.map(lambda w:(w[:1], w[:-1]))
  return ds.batch(batch_size).prefetch(1) # prefetch(1) : dataset 1개(20 단위 데이터)를 미리 준비해 둠. 훈련속도를 더 빠르게 처리
  # ds.batch(batch_size) : 큰 데이터는 메모리에 한번에 올릴 수 없으므로 batch_size 만큼 나누어 학습을 시킴

WINDOW_SIZE = 20
BATCH_SIZE = 32
print()
train_data = window_dadtaset_func(y_train,WINDOW_SIZE, BATCH_SIZE, True) # train_data 섞기
test_data = window_dadtaset_func(y_train,WINDOW_SIZE, BATCH_SIZE, False) # test_data는 섞지 않음
print(train_data)
print(test_data)

for data in train_data.take(1):
  print(data[0].shape) # (32, 1, 1) -> (batch_size, window_size, feature)
  print(data[1].shape) # (32, 20, 1) -> (batch_size, window_size, feature)

# model
from keras.models import Sequential
from keras.layers import Dense, LSTM, Conv1D
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.losses import Huber
from keras.optimizers import Adam

model = Sequential([
    Conv1D(filters=32, kernel_size=5, padding='causal', activation='relu', input_shape=[WINDOW_SIZE, 1]),   # 시간 순서를 위반하지 않는 시계열 데이터를 처리 시 효과적
    LSTM(16, activation='tanh'),
    Dense(16, activation='relu'),
    Dense(1)
])

print(model.summary())

loss = Huber()
optimizer = Adam(learning_rate = 0.0005)
model.compile(loss=loss, optimizer=optimizer, metrics=['mse'])

es = EarlyStopping(monitor='val_loss', patience=10)

history = model.fit(train_data, epochs=100, batch_size=32, validation_data=test_data, verbose=2, callbacks=es)

import numpy as np

pred = model.predict(test_data)
print('예측값 : ',pred[:10].flatten())
print('실제값 : ',np.asarray(y_test)[:10])

# 시각화
import matplotlib.pyplot as plt
plt.figure(figsize=(8,5))
plt.plot(np.asarray(y_test)[20:], label='real')
plt.plot(pred, label='pred', c='blue')
plt.legend()
plt.show()