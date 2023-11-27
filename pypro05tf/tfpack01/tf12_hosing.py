# 다중회귀분석 - 다중 신경망
# 켈리포니아 주택가격

from sklearn.datasets import fetch_california_housing 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import tensorflow as tf 
from keras.models import Sequential 
from keras.layers import Dense, Concatenate 
from keras import optimizers
from sklearn.preprocessing import MinMaxScaler, minmax_scale, StandardScaler, RobustScaler 
import keras
from sklearn.model_selection import train_test_split 

housing = fetch_california_housing()
print(housing.keys())
print(housing.data[:3], type(housing.data))
print(housing.target[:3], type(housing.data))
print(housing.feature_names)
print(housing.target_names)

print(housing.data.shape) # (20640, 8)

x_train_all, x_test, y_train_all, y_test = train_test_split(housing.data, housing.target)
print(x_train_all.shape, x_test.shape, x_train_all.shape, y_test.shape) # (15480, 8) (5160, 8) (15480,) (5160,)

x_train, x_valid, y_train, y_valid = train_test_split(x_train_all, y_train_all, random_state=12, test_size=0.2)
print(x_train.shape, x_valid.shape, y_train.shape, y_valid.shape) # (12384, 8) (3096, 8) (12384,) (3096,)

# scale 조정 : 표준화
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_vaild = scaler.fit_transform(x_valid)
x_test = scaler.fit_transform(x_test)

print('Sequential api : 단순한 MLP ------------')
model = Sequential()
model.add(Dense(units=32, activation='relu',input_shape=x_train.shape[1:]))
model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mse', metrics=['mse'])
history = model.fit(x_train, y_train, epochs=50, validation_data=(x_vaild,y_valid),verbose=1)
print('evaluate : ',model.evaluate(x_test, y_test, verbose=0))
x_new = x_test[:3]
y_pred = model.predict(x_new)
print('예측값 : ',y_pred.ravel())
print('실제값 : ',y_test[:3].ravel())

# 시각화
plt.plot(history.history['mse'], c='b', label='mse') # loss랑 mse 거의 같음
plt.plot(history.history['val_mse'], c='r', label='val_mse') 
plt.xlabel('epochs')
plt.ylabel('mse')
plt.legend()
plt.show()

print('functional api : 복잡하고 유연한 MLP -----------------------')
from keras.layers import Input 
from keras.models import Model

input_ = Input(shape=x_train.shape[1:]) 
net1 = Dense(units=32, activation='relu')(input_)
net2 = Dense(units=32, activation='relu')(net1)
concat = Concatenate()([input_, net2]) # 입력층과 마지막 은닉층을 연결
output = Dense(units=1)(concat)

model2 = Model(inputs=[input_], outputs=[output]) # input, output 여러개 될 수 있으니 s 붙음

model2.compile(optimizer='adam', loss='mse', metrics=['mse'])
history = model2.fit(x_train, y_train, epochs=50, validation_data=(x_vaild,y_valid),verbose=1)
print('evaluate : ',model2.evaluate(x_test, y_test, verbose=0))
x_new = x_test[:3]
y_pred = model2.predict(x_new)
print('예측값 : ',y_pred.ravel())
print('실제값 : ',y_test[:3].ravel())

# 시각화
plt.plot(history.history['mse'], c='b', label='mse') # loss랑 mse 거의 같음
plt.plot(history.history['val_mse'], c='r', label='val_mse') 
plt.xlabel('epochs')
plt.ylabel('mse')
plt.legend()
plt.show()

print('functional api : 일부 특성은 짧은 경로로 전달하고, 다른 특성들은 깊은 경로로 전달  -----------------------')
# 5개 특성(0~4)은 짧은 경로, 6개 특성(2~7)은 긴 경로로 전달
input_a = Input(shape=[5], name='wide_input') # 짧은 경로
input_b = Input(shape=[6], name='deep_input') # 긴 경로
net1 = Dense(units=32, activation='relu')(input_b)
net2 = Dense(units=32, activation='relu')(net1)
concat = Concatenate()([input_a, net2])  # 입력층과 마지막 은닉층을 연결
output = Dense(units=1, name='output')(concat)

model3 = Model(inputs=[input_a, input_b], outputs=[output])
model3.compile(optimizer='adam', loss='mse', metrics=['mse'])

# fit()을 실행할 때 하나의 입력행렬 x_train을 전달하는 것이 아니라
# 입력 마다 하나씩 행렬의 튜플(x_train_a, x_train_b)을 전달행야 한다.
x_train_a, x_train_b = x_train[:, :5], x_train[:,2:]
x_valid_a, x_valid_b = x_valid[:, :5], x_valid[:,2:]
x_test_a, x_test_b = x_test[:, :5], x_test[:,2:] # eval‎uate용
x_new_a, x_new_b = x_test_a[:3], x_test_b[:3] # predict용

history = model3.fit((x_train_a, x_train_b), y_train, epochs=50,
                     validation_data=((x_valid_a, x_valid_b), y_valid), verbose=2)
print('evaluate : ', model3.evaluate((x_test_a, x_test_b), y_test, verbose=0))

y_pred = model3.predict((x_new_a, x_new_b))
print('예측값 : ', y_pred.ravel())
print('실제값 : ', y_test[:3])

# 시각화
plt.plot(history.history['mse'], c='b', label='mse')
plt.plot(history.history['val_mse'], c='r', label='val_mse')
plt.xlabel('epochs')
plt.ylabel('mse')
plt.legend()
plt.show()

