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

print('방법 3 : Subclassing API 사용')
import keras
class MyModel(keras.Model):
    def __init__(self):
        super(MyModel, self).__init__()
        self.conv1 = keras.layers.Conv2D(filters=16, kernel_size=[3,3], padding='valid', activation='relu')
        self.pool1 = keras.layers.MaxPool2D((2,2))
        self.drop1 = keras.layers.Dropout(0.3)
        
        self.conv2 = keras.layers.Conv2D(filters=16, kernel_size=[3,3], padding='valid', activation='relu')
        self.pool2 = keras.layers.MaxPool2D((2,2))
        self.drop2 = keras.layers.Dropout(0.3)
        
        self.flatten = keras.layers.Flatten(dtype='float32')
        
        self.d1 = keras.layers.Dense(units=64, activation='relu')
        self.drop3 = keras.layers.Dropout(0.3)
        
        self.d2 = keras.layers.Dense(units=10, activation='softmax')
        
    def call(self, inputs):
        net = self.conv1(inputs)
        net = self.pool1(net)
        net = self.drop1(net)
        
        net = self.conv2(net)
        net = self.pool2(net)
        net = self.drop2(net)
        
        net = self.flatten(net)
        
        net = self.d1(net)
        net = self.drop3(net)
        
        net = self.d2(net)
        return net
    
model = MyModel()
temp_inputs = keras.layers.Input(shape=(28,28,1))
model(temp_inputs)

print(model.summary())
        
        
        