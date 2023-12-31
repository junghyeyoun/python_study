# -*- coding: utf-8 -*-
"""tfc_30character.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g70-lgJCFelX79cA1tQVgNVVXfICfipk
"""

# 글자 단위 텍스트 생성 모델
filname = 'engdata.txt'

# et = open(filname,encoding='utf-8').read().lower()
# print(et)

# 드라이브 마운트된 파일 읽기
with open('/content/drive/MyDrive/engdata.txt','r',encoding='utf-8') as t:
  et = t.read().lower()

print(et)

# 문자 인덱싱
chars = sorted(list(et))
print(chars)
char_to_int = dict((c, i) for i, c in enumerate(chars))
print(char_to_int)

n_chars = len(et)
n_vocab = len(chars)
print('전체 글자 수 : ',n_chars)
print('전체 어휘 크기 : ',n_vocab)

seq_length = 50   # 학슬할 문자를 해당 숫자 개 씩 끊어서 만들기
datax = []
datay = []

for i in range(0,n_chars - seq_length, 1):
  seq_in = et[i:i+seq_length]
  seq_out = et[i+seq_length]
  # print(seq_in,'/',seq_out)
  datax.append([char_to_int[char] for char in seq_in])
  datay.append(char_to_int[seq_out])

print(datax)
print(datay)

datax_pattern = len(datax)
print('datax_pattern 행렬 유형 수 : ',datax_pattern)

# data 구조 변경
import numpy as np
feature = np.reshape(datax, (datax_pattern, seq_length, 1))
print(feature[:1],feature.shape)

feature = feature/float(n_vocab) # 전체 글자수로 정규화
print(feature[:1])

from keras.utils import to_categorical
label = to_categorical(datay)
print(label[:1])

# model
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from keras.callbacks import EarlyStopping, ModelCheckpoint
import sys
import matplotlib.pyplot as plt

model = Sequential()   # 글자 단위는 Embedding 레이어 없다
model.add(LSTM(units=256, input_shape=(feature.shape[1], feature.shape[2]), activation='tanh', return_sequences=True))
model.add(Dropout(rate=0.2))
model.add(LSTM(units=256, activation='tanh'))
model.add(Dropout(rate=0.2))
model.add(Dense(units=label.shape[1], activation='softmax'))
print(model.summary())

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

chkPoint = ModelCheckpoint('tf29model.hdf5', monitor='loss', verbose=0, save_best_only=True, mode='min')
es = EarlyStopping(monitor='loss', patience=10)
history = model.fit(feature, label, batch_size=32, epochs=500, verbose=2, callbacks=[chkPoint, es])

fig, loss_ax = plt.subplots()
acc_ax = loss_ax.twinx()

loss_ax.plot(history.history['loss'], label='train loss', c='r')
loss_ax.set_xlabel('epochs')
loss_ax.set_xlabel('loss')
loss_ax.legend(loc='upper left')

acc_ax.plot(history.history['accuracy'], label='train accuracy', c='b')
acc_ax.set_xlabel('accuracy')
acc_ax.legend(loc='lower left')

plt.show()

# print('문장 작성 -----------')
int_to_char = dict((i, c) for i, c in enumerate(chars))
print('int_to_char : ', int_to_char)

start = np.random.randint(0, len(datax) -1)
pattern = datax[start]
print('pattern : ', pattern)

print('seed : ')
print("\"", ''.join([int_to_char[value] for value in pattern]), "\"")
print()
for i in range(500):   # 글자 500개로 문장 생성
  x = np.reshape(pattern, (1, len(pattern), 1))
  x = x / float(n_vocab)
  pred = model.predict(x, verbose=0)
  # print(pred)  # [[0.26023662 0.02229353 0.08810616 0.08377218 0.05916742 0.01110107...
  index = np.argmax(pred)
  result = int_to_char[index]  # 인덱스 번째 문자 얻기
  seq_in = [int_to_char[value] for value in pattern]
  # print(result)
  sys.stdout.write(result)
  pattern.append(index)   # 예측된 글자를 누적
  pattern = pattern[1:len(pattern)]

print('종료')