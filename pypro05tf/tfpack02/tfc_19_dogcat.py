# CNN을 이용하여 개, 고양이 이미지 분류 (이항분류)
import tensorflow as tf 
from keras.models import Sequential 
from keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator 
import os 
import numpy as np 
import  matplotlib.pyplot as plt 
import keras

data_url = "https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip"
pathto_zip = keras.utils.get_file('cats_and_dogs.zip', origin=data_url, extract=True) #extract=True -> 압축 풀기
PATH = os.path.join(os.path.dirname(pathto_zip),'cats_and_dogs_filtered')
print(PATH)

batch_size = 128
epochs = 15 
IMG_HEIGHT = 150
IMG_WIDTH = 150

# 데이터 준비
train_dir = os.path.join(PATH, 'train')
validation_dir = os.path.join(PATH, 'validation')

train_cats_dir = os.path.join(train_dir, 'cats')
train_dogs_dir = os.path.join(train_dir, 'dogs')
validation_cats_dir = os.path.join(validation_dir, 'cats')
validation_dogs_dir = os.path.join(validation_dir, 'dogs')
print(train_cats_dir)

num_cats_dir = len(os.listdir(train_cats_dir))
num_dogs_dir = len(os.listdir(train_dogs_dir))
print(os.listdir(train_cats_dir))
num_cats_val = len(os.listdir(validation_cats_dir))
num_dogs_val = len(os.listdir(validation_dogs_dir))

total_train = num_cats_dir + num_dogs_dir
total_val = num_cats_val + num_dogs_val

print('total_train cat : ',num_cats_dir)
print('total_train dog : ',num_dogs_val)
print('total_validation cat : ',num_cats_dir)
print('total_validation dog : ',num_dogs_dir)
print('total_train : ',total_train)
print('total_val : ',total_val)