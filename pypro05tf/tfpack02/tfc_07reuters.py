# 뉴스 기사 다항 분류
# 로이터 뉴스 기사 데이터는 총 11,258개의 뉴스 기사가 46개의 뉴스 카테고리로 분류되는 뉴스 기사 데이터

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.datasets import reuters

#print(reuters.load_data(num_words=10000)) # num_words = 10000 : 자주 쓰이는 만개의 단어만 사용
(train_data, train_label),(test_data, test_label) = reuters.load_data(num_words=10000)
print(train_data.shape, train_label.shape, test_data.shape, test_label.shape) # (8982,) (8982,) (2246,) (2246,)
print(train_data[0])
print(train_label[0])
print(set(train_label))  # 46개

# 숫자로 매핑된 실제 데이터 보기 -------------------------------------
word_index = reuters.get_word_index()
# print(word_index.items()) # dict_items([('mdbl', 10996), ('fawc', 16260), ...
reverse_word_index = dict([value, key] for(key, value) in word_index.items())
# print(reverse_word_index)
# print(train_data[0])
decord_review = ' '.join([reverse_word_index.get(i) for i in train_data[0]])
# print(decord_review)
# ---------------------------------------------------------------

# 데이터
def vector_func(sequences, dim=10000):
    results = np.zeros((len(sequences), dim))
    for i, seq in enumerate(sequences):
        results[i, seq] = 1.
    return results

x_train = vector_func(train_data) # train_data를 벡터화
x_test = vector_func(test_data) # test_data를 벡터화

# import sys
# np.set_printoptions(threshold=sys.maxsize)
# print(x_train[0])

print(train_label[0])
# label은 원핫 처리
'''
def to_onehot_func(labels, dim=46):
    results = np.zeros((len(labels), dim))
    for i, label in enumerate(labels):
        results[i, label] = 1.
    return results

one_hot_train_labels = to_onehot_func(train_label)
print(one_hot_train_labels[0])
'''
# 원핫 처리용 함수 사용
one_hot_train_labels = to_categorical(train_label)
one_hot_test_labels = to_categorical(test_label)
print(one_hot_train_labels[0]) # 56번째 줄이랑 결과 같음

# 네트워크 구성
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(10000,)))
model.add(Dense(64, activation='relu'))
model.add(Dense(46, activation='softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['acc'])

# vaildation data : 선택적
x_val = x_train[:1000]
partial_x_train = x_train[1000:]
print(x_val.shape, partial_x_train.shape) # (1000, 10000) (7982, 10000)
y_val = one_hot_train_labels[:1000]
partial_y_train = one_hot_train_labels[1000:]
print(y_val.shape, partial_y_train.shape) # (1000, 46) (7982, 46)

history = model.fit(x=partial_x_train, y=partial_y_train, epochs=20, batch_size=512, validation_data=(x_val, y_val), verbose=2)

# 시각화 
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss) +1)

plt.plot(epochs, loss, 'bo', label='train loss')
plt.plot(epochs, val_loss, 'r', label='val loss')
plt.xlabel('epochs')
plt.legend()
plt.show()

results = model.evaluate(x_test, one_hot_test_labels, batch_size=512, verbose=0)
print('results  : ', results)

# pred 
pred = model.predict(x_test[:3])
print(pred[0].shape)
print(np.sum(pred[0]))
print('예측 값 : ',pred)
print('예측 값 : ',np.argmax(pred, axis=1))
print('실제 값 : ',np.argmax(one_hot_test_labels[:3], axis=1))