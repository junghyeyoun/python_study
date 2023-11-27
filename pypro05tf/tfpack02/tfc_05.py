# 이항분류는 다항분류로 처리 가능
# dtabets dataset 사용
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical

dataset = np.loadtxt('../testdata/diabetes.csv', delimiter=',')
print(dataset[0], dataset.shape)  # (759, 9)
print(set(dataset[:, -1]))  # {0.0, 1.0} 이항분류 대상

x_train, x_test, y_train, y_test = train_test_split(dataset[:, 0:8], dataset[:, -1],
                                                    test_size=0.3, random_state=123)
print(x_train[:2])
print(y_train[:2])
print('모델1 : 최종 활성화 함수 sigmoid 사용')
model = Sequential()
model.add(Dense(64, input_dim=8, activation='relu'))
# 양수일땐 1, 나머지는 0으로 처리 : relu
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
model.fit(x_train, y_train, epochs=200, batch_size=32, verbose=0)
scores = model.evaluate(x_test, y_test, batch_size=32, verbose=0)
print('%s:%.2f%%'%(model.metrics_names[1], scores[1] * 100))
print('%s:%.2f'%(model.metrics_names[0], scores[0]))

x_new = [[-0.0588235, 0.20603, 0., 0., 0., -0.105812, -0.910333, -0.433333]]
pred = model.predict(x_new, batch_size=32, verbose=0)
print('분류 결과 : ', pred, ' ', np.where(pred > 0.5, 1, 0))
print()

print('\n모델2 : 최종 활성화 함수 softmax 사용')
y_train = to_categorical(y_train, num_classes=2)
print(y_test[0])
y_test = to_categorical(y_test)
print(y_test[0])

model2 = Sequential()
model2.add(Dense(64, input_dim=8, activation='relu'))
# 양수일땐 1, 나머지는 0으로 처리 : relu
model2.add(Dense(32, activation='relu'))
model2.add(Dense(2, activation='softmax'))

model2.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
#loss='sparse_categorical_crossentropy' label에 대해 내부적으로 one_hot 처리함. 학습시 label에 one_hot처리하지 않아야 한다

model2.fit(x_train, y_train, epochs=200, batch_size=32, verbose=0)
scores = model2.evaluate(x_test, y_test, batch_size=32, verbose=0)
print('%s:%.2f%%'%(model2.metrics_names[1], scores[1] * 100))
print('%s:%.2f'%(model2.metrics_names[0], scores[0]))

x_new = [[-0.0588235, 0.20603, 0., 0., 0., -0.105812, -0.910333, -0.433333]]
pred = model.predict(x_new, batch_size=32, verbose=0)
print('분류 결과 : ', pred, ' ', np.argmax(pred))
print()


















