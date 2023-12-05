# -*- coding: utf-8 -*-
"""tfc_17.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PClWr4O6CU57lljol_w4uatXEZd06cXX
"""

import tensorflow as tf
import matplotlib.pyplot as plt
import tensorflow as tf
import sys
import numpy as np
import keras

(x_train, y_train), (x_test, y_test) = keras.datasets.fashion_mnist.load_data()
print(x_train.shape, y_train.shape, x_test.shape, y_test.shape)  # (60000, 28, 28) (60000,) (10000, 28, 28) (10000,)
class_names = ['T-shirt/top', 'Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankel boot']
print(set(y_train))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}'

x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255
x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255
y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

model = keras.models.Sequential([
    keras.layers.Conv2D(filters=32, kernel_size=(3,3), strides=(1,1), padding='same',
                              activation='relu', input_shape=(28, 28, 1)),
    keras.layers.MaxPool2D(pool_size=(2,2)),
    keras.layers.Dropout(rate=0.3),

    keras.layers.Conv2D(filters=32, kernel_size=(3,3), strides=(1,1), padding='same', activation='relu'),
    keras.layers.MaxPool2D(pool_size=(2,2)),
    keras.layers.Dropout(rate=0.3),

    keras.layers.Flatten(),

    # 첫 번째 완전 연결층
    keras.layers.Dense(units=64, activation='relu'),
    keras.layers.Dropout(rate=0.3),

    keras.layers.Dense(units=64, activation='relu'),
    keras.layers.Dropout(rate=0.3),

    keras.layers.Dense(units=10, activation='softmax')
])

print(model.summary())

# 우리가 설계 한 내용
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

from keras.callbacks import EarlyStopping,ModelCheckpoint
import os

MODEL_DIR = './model2/'
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)
modelpath = MODEL_DIR + '{epoch:02d}-{val_loss:.4f}.keras'

es = EarlyStopping(monitor='val_loss', patience=5)

history = model.fit(x_train, y_train, batch_size=64, epochs=500, verbose=2, validation_split=0.2, callbacks=[es])

print(history.history)

# 모델평가
train_loss, train_acc = model.evaluate(x_train, y_train)
test_loss, test_acc = model.evaluate(x_test, y_test)
print('train loss, train_acc : ', train_loss, train_acc)
print('test_loss, test_acc : ', test_loss, test_acc)

history = history.history

import matplotlib.pyplot as plt

# 시각화
def plot_acc(title=None):
    plt.plot(history['accuracy'], label = 'accuracy')
    plt.plot(history['val_accuracy'], label='val_accuracy')
    plt.title(title)
    plt.legend()

plot_acc('accuracy')
plt.show()

print()
def plot_loss(title=None):
    plt.plot(history['loss'], label = 'loss')
    plt.plot(history['val_loss'], label='val_loss')
    plt.title(title)
    plt.legend()

plot_loss('loss')
plt.show()

# VGGNet style 네트워크
# dataset은 Fashion MNIST with CNN
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(input_shape=(28,28,1), kernel_size=(3,3), filters=32, padding='same', activation='relu'),
    tf.keras.layers.Conv2D(kernel_size=(3,3), filters=64, padding='same', activation='relu'),
    tf.keras.layers.MaxPool2D(pool_size=(2,2)),
    tf.keras.layers.Dropout(rate=0.5),
    tf.keras.layers.Conv2D(kernel_size=(3,3), filters=128, padding='same', activation='relu'),
    tf.keras.layers.Conv2D(kernel_size=(3,3), filters=256, padding='valid', activation='relu'),
    tf.keras.layers.MaxPool2D(pool_size=(2,2)),
    tf.keras.layers.Dropout(rate=0.5),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(units=512, activation='relu'),
    tf.keras.layers.Dropout(rate=0.5),
    tf.keras.layers.Dense(units=256, activation='relu'),
    tf.keras.layers.Dropout(rate=0.5),
    tf.keras.layers.Dense(units=10, activation='softmax')
])
model.compile(optimizer=tf.keras.optimizers.Adam(), loss='categorical_crossentropy', metrics=['accuracy'])
print(model.summary())

from keras.callbacks import EarlyStopping
es = EarlyStopping(monitor='val_loss', patience=5)

history = model.fit(x_train, y_train, batch_size=64, epochs=500, verbose=2, validation_split=0.2,
                    callbacks=[es])

print(history.history)

# 모델평가
train_loss, train_acc = model.evaluate(x_train, y_train)
test_loss, test_acc = model.evaluate(x_test, y_test)
print('train loss, train_acc : ', train_loss, train_acc)
print('test_loss, test_acc : ', test_loss, test_acc)

history = history.history

import matplotlib.pyplot as plt

# 시각화
def plot_acc(title=None):
    plt.plot(history['accuracy'], label = 'accuracy')
    plt.plot(history['val_accuracy'], label='val_accuracy')
    plt.title(title)
    plt.legend()

plot_acc('accuracy')
plt.show()

print()
def plot_loss(title=None):
    plt.plot(history['loss'], label = 'loss')
    plt.plot(history['val_loss'], label='val_loss')
    plt.title(title)
    plt.legend()

plot_loss('loss')
plt.show()
