# keras 라이브러리를 사용하여 네트워크 구성
# 간단한 논리회로 분류 모델

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from keras.optimizers import SGD, RMSprop, Adam

# 1. 데이터 수집 및 가공
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # feature
y = np.array([0,1,1,1])  # or / label
# 노드 한 쓰면 xor은 해결 못함 노드의 개수 늘려주면 해결 가능

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
# 클래스를 등장시켜도 되고 클래스를 객체를 만든 것을 써도 됨 / 클래스를 사용하면 기본값을 수정할 수 있는 장점이 있음.
# model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])
# model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy']) # 가장 많이 씀
# model.compile(optimizer=SGD(learning_rate=0.01), loss='binary_crossentropy', metrics=['accuracy']) # learning_rate : 학습율 / 너무 커지면 제대로된 w값을 찾을 수 없다.
# model.compile(optimizer=SGD(learning_rate=0.01, momentum=0.9), loss='binary_crossentropy', metrics=['accuracy'])
# model.compile(optimizer=RMSprop(learning_rate=0.001, momentum=0.9), loss='binary_crossentropy', metrics=['accuracy']) # 0.001이 기본값, 모멘텀에 빠지는 현상 보안
model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy']) # 둘다 보안
# optimizer : 입력데이터와 손실함수를 업데이트하는 메커니즘이다. 손실함수의 최소값을 찾는 알고리즘이다.

# 4. 모델 학습시키기(train) : 더 나은 표현(w를 갱신)을 찾는 자동화 과정
model.fit(x, y, epochs=500, batch_size=1, verbose=2) # epochs=5 : 5번 학습 / verbose=0 진행과정 안보임 보고 싶으면 1로
# batch_size : 훈령데이터를 여러개의 작음 묶음(batch)으로 만들어 가중치(w)를 갱신. 1 epoch시 사용하는 dataset의 크기 

# 5. 모델 평가(test)
loss_metrics = model.evaluate(x, y, batch_size=1, verbose=0)
print(loss_metrics)

# 6. 학습 결과 확인 : 예측값 출력
pred = model.predict(x, batch_size=1, verbose=0)

pred = (model.predict(x) > 0.5).astype('int32')
print('예측 결과 : ', pred.flatten())

# 7. 모델 저장
model.save('tf04model.h5') # hdf5

# 8. 모델 읽기
from keras.models import load_model
mymodel = load_model('tf04model.h5')
