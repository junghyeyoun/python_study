# -*- coding: utf-8 -*-
"""tfc_43bilstm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S8lv23wp5lq70BgryMkm_6-ggJMK5PDc
"""

# ex) --- Bidirectional LSTM on IMDB ---
import numpy as np
from tensorflow import keras
from keras import layers

max_features = 20000  # 상위 20000개 단어만을 사용하겠다.
maxlen = 200             # 영화 리뷰 중 처음 200 단어까지만 사용.

# Build the model : 가변 길이의 정수형 시퀀스를 input으로 사용.
inputs = keras.Input(shape=(None, ), dtype="int32")
x = layers.Embedding(max_features, 128)(inputs)  # 각 정수형 시퀀스를 128차원으로 임베딩 처리함.

# Bidirectional LSTM layer를 두 번 사용.
x = layers.Bidirectional(layers.LSTM(64, return_sequences=True))(x)
x = layers.Bidirectional(layers.LSTM(64))(x)
outputs = layers.Dense(1, activation="sigmoid")(x)  # 이진 분류
model = keras.Model(inputs, outputs)
print(model.summary())


# IMDB 영화 리뷰 감정 데이터 로딩
(x_train, y_train), (x_val, y_val) = keras.datasets.imdb.load_data(num_words=max_features)
print(len(x_train), "Training sequences")
print(len(x_val), "Validation sequences")

# pad_sequences
x_train = keras.preprocessing.sequence.pad_sequences(x_train, maxlen=maxlen)
x_val = keras.preprocessing.sequence.pad_sequences(x_val, maxlen=maxlen)

# Train and eval‎uate the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
history = model.fit(x_train, y_train, batch_size=32, epochs=2, validation_data=(x_val, y_val), verbose=2)
print(history.history)