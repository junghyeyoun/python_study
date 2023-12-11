# -*- coding: utf-8 -*-
"""tfc_36_spammail.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uB5gryctqtOy8gOfdugcQMZBrakTps35
"""

# 스팸 메일 분류 (이항 분류) : LSTM 이용 -> many to one
import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/spam.csv', encoding='latin1')
print(data.head(3))
del data['Unnamed: 2']
del data['Unnamed: 3']
del data['Unnamed: 4']
print(data.head(3))
data['v1'] = data['v1'].replace(['ham','spam'], [0,1])
print(data.head(3))
print(data.info())
print(data.isnull()) # 결측치 없음

print(data['v2'].nunique()) # 전체 5572개 중 5169만 유니크함. 따라서 중복된 값 있음
# 중복 메일 제거
data.drop_duplicates(subset=['v2'], inplace=True)
print('행 수 : ',len(data))
print(data['v1'].value_counts()) # 0  :  4516 / 1   :  653
print(data.groupby('v1').size().reset_index(name='count'))

x_data = data['v2'] # 메일 내용 (feature)
y_data = data['v1'] # 메일 구분 (label)

# feature에 대한 토큰 처리
from keras.preprocessing.text import Tokenizer
tok = Tokenizer() # char_level=False : 단어(기본), char_level=True : 글자
tok.fit_on_texts(x_data)
sequences = tok.texts_to_sequences(x_data)
print(sequences[:3])

word_to_index = tok.word_index
print(word_to_index)
print(x_data[:1])

vocab_size = len(word_to_index) + 1
print('vocab_size : ',vocab_size)

x_data = sequences
print('max len : ',max(len(i) for i in x_data)) # 189
print('avg len:', (sum(map(len, x_data)) / len(x_data)))  # 15.610369510543626

from keras.utils import pad_sequences
max_len = max(len(i) for i in x_data)
data = pad_sequences(x_data, maxlen=max_len)
print(data[:1])

# train, test split
n_of_train = int(len(sequences)*0.8)
n_of_test = int(len(sequences) - n_of_train)
print('n_of_train : ', n_of_train)
print('n_of_test : ', n_of_test)
import numpy as np
x_train = data[:n_of_train]
y_train = np.array(y_data[:n_of_train])
x_test = data[n_of_train:]
y_test = np.array(y_data[n_of_train:])
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
print(x_train[:2])
print(y_train[:2])

# model : LSTM + Dense
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, Embedding

model = Sequential()
model.add(Embedding(vocab_size, 32))
model.add(LSTM(units=32, activation='tanh'))
model.add(Dense(units=32, activation='relu'))
model.add(Dropout(rate=0.2))
model.add(Dense(units=1, activation='sigmoid'))

print(model.summary())

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
history = model.fit(x=x_train, y=y_train, batch_size=32, epochs=5, validation_split=0.2, verbose=2)

print('test로 검증된 분류 정확도 : %.3f'%(model.evaluate(x_test, y_test)[1]))

# 시각화
import matplotlib.pyplot as plt
epochs = range(1, len(history.history['acc'])+1)
plt.plot(epochs, history.history['acc'], label='accuracy')
plt.plot(epochs, history.history['val_acc'], label='val_accuracy')
plt.ylabel('acc')
plt.legend()
plt.show()

plt.plot(epochs, history.history['loss'], label='loss')
plt.plot(epochs, history.history['val_loss'], label='val_loss')
plt.ylabel('loss')
plt.legend()
plt.show()

# pred
pred = model.predict(x_test[:20])
print('예측값 : ',np.where(pred>0.5, 1, 0).flatten())
print('실제값 : ',y_test[:20])