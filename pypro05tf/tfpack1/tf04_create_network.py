import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np

# 1. 데이터 수집 및 가공
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # feature
y = np.array([0,1,1,1])  # or / label

# 2. 모델 구성(설정)
# model = Sequential([
#     Dense(input_dim=2, units=1),
#     Activation('sigmoid')
# ])
model = Sequential()
model.add(Dense(units=1, input_dim=2))
model.add(Activation('sigmoid'))
# model.add(Dense(units=1, input_dim=2, activation = 'sigmoid')) # 합쳐서 쓰기

# 3. 모델 학습 과정 설명(컴파일)
model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

# 4. 모델 학습시키기
model.fit(x, y, epochs=500, batch_size=1, verbose=2) # epochs=5 : 5번 학습 / verbose=0 진행과정 안보임 보고 싶으면 1로

# 5. 모델 평가
loss_metrics = model.evaluate(x, y, batch_size=1, verbose=0)

# 6. 학습 결과 확인 : 예측값 출력
pred = model.predict(x, batch_size=1, verbose=0)













pred = (model.predict(x) > 0.5).astype('int32')
print('예측 결과 : ', pred.flatten())
