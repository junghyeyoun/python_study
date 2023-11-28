# CNN은 Convolutinal Neural Networks의 약자로 딥러닝에서 주로 이미지나 영상 데이터를 처리할 때 쓰이며 이름에서
# 알 수 있다시피 Convolutinal이라는 전처리 작업이 들어가는 Neural Networks 모델
# 특징추출 알고리즘 사용 : 이미지나 텍스트 데이터를 conv와 pooling을 반복하여 데이터 양을 줄인 후 완전연결층으로 전달해 분류 작업을 실행한다.

import tensorflow as tf  
import sys 
import numpy as  np 
import keras

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)
print(x_train[0]) # 0번째 feature
print(y_train[0]) # 0번째 label

# cnn은 채널(channel)을 사용하므로 3차원을 4차원으로 변환
x_train = x_train.reshape((60000,28,28,1))  # (-1,28,28,1)으로 써도 됨  -1은 데이터의 크기 알아서 정해달라는 뜻
x_test = x_test.reshape((10000,28,28,1))
print(x_train.shape, x_test.shape)
print(x_train[:1]) # 4차원

x_train = x_train / 255.0 # 정규화
x_test = x_test / 255.0

# 모델 ( CNN : 고해상도 크기가 큰 이미지를 전처리 후 작은 이미지로 변환을 후 ==>  Dense(완전연결층)으로 전달
input_shape = (28,28,1)

print('방법 1 : Sequential API')
model = keras.models.Sequential()

# Conv2D(필터수, 필터크기, 스트라이드(필터이동량), 패딩여부,...)
# padding='valid': 원본이미지 밖에 0으로 채우기를 안함 / same : 0으로 채우기를 함
# Conv(합성곱) : 필터를 이미지 일부분과 픽셀끼리 곱한 후, 결과를 더함
model.add(keras.layers.Conv2D(filters=16, kernel_size=(3,3),strides=(1,1), padding='valid', activation='relu', input_shape=input_shape))

# pooling : 이미지 특징을 유지한 채로 크기를 줄임
model.add(keras.layers.MaxPool2D(pool_size=(2,2))) # 필수 아님. 선택사항
model.add(keras.layers.Dropout(rate=0.3)) # 과적합 방지

model.add(keras.layers.Conv2D(filters=32, kernel_size=(3,3),strides=(1,1), padding='valid', activation='relu'))
model.add(keras.layers.MaxPool2D(pool_size=(2,2)))
model.add(keras.layers.Dropout(rate=0.3))

model.add(keras.layers.Conv2D(filters=64, kernel_size=(3,3),strides=(1,1), padding='valid', activation='relu'))
model.add(keras.layers.MaxPool2D(pool_size=(2,2)))
model.add(keras.layers.Dropout(rate=0.3))

model.add(keras.layers.Flatten()) # FCLayer (Fully Connected Layer) : 이미지를 1차원으로 변경

# Dense 
model.add(keras.layers.Dense(units=64, activation='relu'))
model.add(keras.layers.Dropout(rate=0.2))
model.add(keras.layers.Dense(units=31, activation='relu'))
model.add(keras.layers.Dropout(rate=0.2))
model.add(keras.layers.Dense(units=10, activation='softmax'))

print(model.summary())

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

from keras.callbacks import EarlyStopping 
es = EarlyStopping(monitor='val_loss', patience=3)

history = model.fit(x_train, y_train, batch_size=128, epochs=100, verbose=1, validation_split=0.2, callbacks=es)
print(history.history)

# 모델 평가
train_loss, train_acc = model.evaluate(x_train, y_train)
test_loss, test_acc = model.evaluate(x_test, y_test)
print('train_loss, train_acc : ',train_loss, train_acc)
print('test_loss, test_acc : ',test_loss, test_acc)

# -------------------------------------
import pickle
history = history.history # history를 객체로 저장 
with open('tfc_13his.pickle','wb') as obj:
    pickle.dump(history, obj)

with open('tfc_13his.pickle','rb') as obj:
    history = pickle.load(obj)

# 시각화 
import matplotlib.pyplot as plt
def plot_acc(history):
    plt.plot(history['accuracy'], label='accuracy')
    plt.plot(history['val_accuracy'], label='val_accuracy')
    plt.title('Accuracy')
    plt.legend()

def plot_loss(history):
    plt.plot(history['loss'], label='loss')
    plt.plot(history['val_loss'], label='val_loss')
    plt.title('Loss')
    plt.legend()

plot_acc(history)
plt.show()

plot_loss(history)
plt.show()

# 모델 저장
model.save('tfc_13_model.h5')

# ------------------------------
# 새이미지 분류 작업 ... 
print('예측값 : ',np.argmax(model.predict(x_test[:1])))
print('예측값 : ',np.argmax(model.predict(x_test[[[0]]]))) # 위와 같은 내용
print('실제값 : ',y_test[0])