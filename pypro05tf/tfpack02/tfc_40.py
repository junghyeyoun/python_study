# -*- coding: utf-8 -*-
"""tfc_40.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IoNdks19meCW7IEvG_k9Q-16xcnluRro
"""

# 로이터 뉴스 데이터로 다항분류
# 네트워크 구성을 4가지로 작성 후 비교 : Dense, RNN + Dense, CNN + Dense, CNN + RNN + Dense

from keras.datasets import reuters
from keras.models import Sequential
from keras.layers import LSTM, Embedding, Dense, Flatten, Conv1D, GlobalMaxPooling1D, Dropout
import tensorflow as tf
from keras.utils import pad_sequences, to_categorical
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = reuters.load_data(num_words=10000) # 46개의 범주
print(x_train.shape,y_train.shape, x_test.shape, y_test.shape)
print(x_train[0])
print(y_train[0])

# train / validation
x_val = x_train[7000:]
y_val = y_train[7000:]
x_train = x_train[:7000]
y_train = y_train[:7000]

# 문장 길이 맞추기
text_max_words = 120
x_train = pad_sequences(x_train, maxlen=text_max_words) # feature
x_val = pad_sequences(x_val, maxlen=text_max_words)
x_test = pad_sequences(x_test, maxlen=text_max_words)
print(x_train[0], len(x_train[0]))

y_train = to_categorical(y_train) # label
y_val = to_categorical(y_val)
y_test = to_categorical(y_test)
print(y_train[0])

# 모델 구성 1 : 완전 연결층만 사용
model = Sequential()
model.add(Embedding(10000,128,input_length=text_max_words))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(46, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print(model.summary())

hist = model.fit(x_train, y_train, epochs=10, batch_size=64, validation_data=(x_val, y_val), verbose=2)

# 시각화
def plot_func():
  fig, loss_ax = plt.subplots()
  acc_ax = loss_ax.twinx()
  loss_ax.plot(hist.history['loss'], 'y', label='train loss')
  loss_ax.plot(hist.history['val_loss'], 'r', label='validation loss')
  loss_ax.set_ylim([0.0,3.0])

  acc_ax.plot(hist.history['accuracy'], 'b', label='train accuracy')
  acc_ax.plot(hist.history['val_accuracy'], 'g', label='validation accuracy')
  acc_ax.set_ylim([0.0,3.0])

  loss_ax.set_xlabel('epoch')
  loss_ax.set_ylabel('epoch')
  acc_ax.set_ylabel('accuracy')

  loss_ax.legend(loc='upper left')
  acc_ax.legend(loc='lower left')

  plt.show()

  print('eval : ', model.evaluate(x_test, y_test, batch_size=64, verbose=0))

plot_func()

# 모델 구성 2 : RNN + 완전 연결층 사용
model = Sequential()
model.add(Embedding(10000,128))
model.add(LSTM(128))
model.add(Dense(256, activation='relu'))
model.add(Dense(46, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print(model.summary())

hist = model.fit(x_train, y_train, epochs=10, batch_size=64, validation_data=(x_val, y_val), verbose=2)

plot_func()

# 모델 구성 3 : CNN + 완전 연결층 사용
model = Sequential()
model.add(Embedding(10000,128,input_length=text_max_words))
model.add(Conv1D(256, 3, padding='valid', activation='relu',strides=1))
model.add(GlobalMaxPooling1D())
model.add(Dense(256, activation='relu'))
model.add(Dense(46, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print(model.summary())

hist = model.fit(x_train, y_train, epochs=10, batch_size=64, validation_data=(x_val, y_val), verbose=2)

plot_func()

# 모델 구성 4 : CNN + RNN + 완전 연결층 사용
from keras.layers import MaxPooling1D
model = Sequential()
model.add(Embedding(10000,128,input_length=text_max_words))
model.add(Conv1D(256, 3, padding='valid', activation='relu',strides=1))
model.add(MaxPooling1D(pool_size=4))
model.add(LSTM(128))
model.add(Dense(256, activation='relu'))
model.add(Dense(46, activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
print(model.summary())

hist = model.fit(x_train, y_train, epochs=10, batch_size=64, validation_data=(x_val, y_val), verbose=2)

plot_func()