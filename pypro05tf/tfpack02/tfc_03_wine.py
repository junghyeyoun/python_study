# red & white dataset으로 이항분류 모델
import os.path

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

wdf = pd.read_csv('../testdata/wine.csv', header=None)
print(wdf.head(2))
print(wdf.info())
print(wdf.iloc[:,12].unique())
print(len(wdf[wdf.iloc[:, 12]==0]))  # 4898 red
print(len(wdf[wdf.iloc[:, 12]==1]))  # 1599 white

dataset = wdf.values  # values를 써주면 int는 자동으로 float으로 바뀜
x = dataset[:, :12]
y = dataset[:, -1]
print(x[0])
print(y[0])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=12)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

model = Sequential()
model.add(Dense(units=32, input_dim=12, activation='relu'))  # 혹은 input_shape=(12,)
model.add(Dense(16, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
print(model.summary())

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

loss, acc = model.evaluate(x=x_train, y=y_train, verbose=2)
print('훈련 안 한 모델 정확도 : {:5.2f}%'.format(acc * 100))  # 74.86%

MODEL_DIR = './model/'
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)
    # 경로가 존재하지 않으면 생성

fname = 'tfc_3.hdf5'
chkpoint = ModelCheckpoint(MODEL_DIR + fname, monitor='val_loss', verbose=0, save_best_only=True)
# save_best_only=True 이걸 써주면 loss가 떨어질 때만 기록. 안 쓰면 올라갈 때 내려갈 때 모두 저장.
early_stop = EarlyStopping(monitor='val_loss', mode='auto', patience=10)  # model : {'auto', 'min', 'max'}
# acc니까 점점 높아져야하니 max, loss일땐 min을 써야겠지. auto써주면 monitor보고 알아서 판단함
history = model.fit(x=x_train, y=y_train, epochs=1000, batch_size=64,
                    validation_split=0.3, callbacks=[early_stop, chkpoint])
# validation_split쓰면 웬만하면 monitor='val_loss'써줌. (학습 도중의 loss?)
# patience = 5를 주면 5회동안 모델이 더 좋아지지 않으면 강제로 모델 학습을 끝냄

loss, acc = model.evaluate(x=x_test, y=y_test, verbose=2)
print('훈련 한 모델 정확도 : {:5.2f}%'.format(acc * 100))  # 94.00%

# 시각화
epoch_len = np.arange(len(history.epoch))

plt.plot(epoch_len, history.history['loss'], c='red', label='loss')
plt.plot(epoch_len, history.history['val_loss'], c='blue', label='val_loss')  # 이 둘의 차이가 크면 안 좋음
plt.xlabel('epochs')
plt.ylabel('loss')
plt.legend(loc='best')
plt.show()

plt.plot(epoch_len, history.history['accuracy'], c='red', label='accuracy')
plt.plot(epoch_len, history.history['val_accuracy'], c='blue', label='val_accuracy')  # 이 둘의 차이가 크면 안 좋음
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend(loc='best')
plt.show()
# 37번째 줄에 metrics=['accuracy']가 acc라면 시각화도 acc라 해야됨

print('-----------------')
# 가장 우수한 모델로 저장된 파일을 읽어 분류 예측
from keras.models import load_model
mymodel = load_model(MODEL_DIR + fname)
new_data = x_test[:5, :]
pred = mymodel.predict(new_data)
print('pred : ', np.where(pred > 0.5, 1, 0).flatten())