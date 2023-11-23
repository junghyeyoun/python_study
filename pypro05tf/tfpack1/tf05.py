# keras 라이브러리를 사용하여 네트워크 구성
# 간단한 논리회로 분류 모델

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from keras.optimizers import SGD, RMSprop, Adam

x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # feature
y = np.array([0,1,1,0])  # xor

model = Sequential()
# model.add(Dense(units=1, input_dim=2, activation = 'sigmoid')) # 합쳐서 쓰기
# model.add(Dense(units=5, input_dim=2))
# model.Add(Activation('relu')) # relu : Sigmoid와 tanh가 갖는 Gradient Vanishing 문제를 해결하기 위한 함수이다.
# Gradient Vanishing(기울기 소실) 문제는 Back Propagation에서 계산 결과와 정답과의 오차를 통해 가중치를 수정하는데,
# 입력층으로 갈수록 기울기가 작아져 가중치들이 업데이트 되지 않아 최적의 모델을 찾을 수 없는 문제이다.
# model.add(units=1) # 노드 한개 추가
# model.add(Activation('sigmoid')) # 분류니까 sigmoid 씀

# 위에 주석 다 합쳐서 쓰는 방법 / layer 3개
model.add(Dense(units=5, input_dim=2, activation = 'relu')) # hidden layer node에서 씀
model.add(Dense(units=5, activation = 'relu'))
model.add(Dense(units=1, activation = 'sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(x, y, epochs=1000, batch_size=1, verbose=2)
loss_metrics = model.evaluate(x, y)
print(loss_metrics)

pred = model.predict(x, batch_size=1, verbose=0)

pred = (model.predict(x) > 0.5).astype('int32')
print('예측 결과 : ', pred.flatten())

print(model.summary())

print()
print('input------')
print(model.input)
print('output------')
print(model.output)
print('weights------')
print(model.weights)

print('**'*20)
#print(history.history) # loss와 accuracy dict  type으로 보여줌
print(history.history['loss'])
print(history.history['accuracy'])

# 시각화 
import matplotlib.pyplot as plt
plt.plot(history.history['loss'], label='train loss')
plt.xlabel('epochs')
plt.legend()
plt.show()

plt.plot(history.history['accuracy'], label='train accuracy')
plt.xlabel('epochs')
plt.legend()
plt.show()

import pandas as pd 
pd.DataFrame(history.history)['loss'].plot(figsize=(8,5))
plt.show()