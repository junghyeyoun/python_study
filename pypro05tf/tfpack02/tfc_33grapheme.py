# -*- coding: utf-8 -*-
"""tfc_33grapheme.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11KX9xd80P5FWSE-UZDsuva3P6bsy9o18
"""

# token이 자소 단위인 데이터로 자연어 생성 모델 작성
!pip install jamotools

import jamotools
import tensorflow as tf
import numpy as np
import keras

path = keras.utils.get_file(
    'rnn_short_toji.txt',
    origin='https://raw.githubusercontent.com/pykwon/etc/master/rnn_short_toji.txt')
text = open(path, 'rb').read().decode(encoding='utf-8')

print('전체 글자 수 : {}'.format(len(text)))
print(text[:100])

# 한글 자료 자모 단위로 분리. 한자에는 영향이 없다.
# s_split = jamotools.split_syllables(text[:50]) # 잘라주기
# print(s_split)
# rever = jamotools.join_jamos(s_split) # 다시합쳐주기
# print(rever)

train_text_x = jamotools.split_syllables(text)

# 단어 사전
vocab = sorted(set(train_text_x))
vocab.append('UNK')
print('{}unique words'.format(len(vocab))) # 179unique words

# 단어 인덱싱
char2idx = {w: i for i, w in enumerate(vocab)}
# print(char2idx)
idx2char = np.array(vocab)
print(idx2char)
text_as_int = np.array([char2idx[c] for c in train_text_x])
print(text_as_int)

print(train_text_x[:20])
print(text_as_int[:20])

# dataset 작성
seq_length = 80 # 80개의 자모가 주어질 경우 다음 자모를 예측
example_per_epoch = len(text_as_int) // seq_length
print(example_per_epoch)

import tensorflow as tf
char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int) # 전체가 아니라 부분 데이터 읽기
char_dataset = char_dataset.batch(seq_length + 1, drop_remainder=True)
# seq_length + 1 : 처음 25개 단어와 그 뒤에 나오는 정답(label)이 될 한 단어를 합쳐 반환하기 위함
# drop_remainder=True : 마지막 배치 크기를 무시

for item in char_dataset.take(1): # batch를 한번씩 불러옴 -> 데이터가 양이 많을 때 이렇게 불러옴(청크처럼)
  print(item.numpy())
  print(idx2char[item.numpy()])

def split_input_target(chunk):
  return [chunk[:-1],chunk[-1]] # [25단어].1단어

train_dataset = char_dataset.map(split_input_target)

for x, y in train_dataset.take(1):
  print(idx2char[x.numpy()])
  print(x.numpy())
  print(idx2char[y.numpy()])
  print(y.numpy())

# model
BATCH_SIZE = 64
steps_per_epoch = example_per_epoch // BATCH_SIZE
BUFFER_SIZE = 5000

# suffle을 사용하면 epoch마다 Dataset을 섞을 수 있다.
train_dataset = train_dataset.shuffle(buffer_size=BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

total_chars = len(vocab)
print(total_chars) # 54048

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(total_chars, 100, input_length=seq_length), # 자모단위도 Embedding 줌
    tf.keras.layers.LSTM(units=256, return_sequences=True),
    tf.keras.layers.Dropout(rate=0.2),
    tf.keras.layers.LSTM(units=256),
    tf.keras.layers.Dense(units=total_chars, activation='relu'),
    tf.keras.layers.Dense(units=total_chars, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print(model.summary())

# 단어 단위 생성 모델 학습
from keras.preprocessing.sequence import pad_sequences

def testmodelFunc(epoch, logs):
  if epoch % 5 != 0 and epoch != 49: # 5의 배수이거나 49이면 처리
    return

  test_sentence = text[0]
  test_sentence = jamotools.split_syllables(test_sentence)

  next_chars = 300
  for _ in range(next_chars):
    test_text_x = test_sentence[-seq_length:] # 임의의 문장 뒤에서 부터 seq_length(25) 만큼 선택
    test_text_x = np.array(idx2char[c] if c in idx2char else idx2char['UNK'] for c in test_text_x)
    test_text_x = pad_sequences([test_text_x], maxlen=seq_length, padding='pre', value=idx2char['UNK'])
    ouput_idx = np.argmax(model.predict(test_text_x), axis=-1) # 출력 값 중에서 가장 값이 큰 인덱스 반환
    test_sentence += ' ' + idx2char[ouput_idx[0]] # 출력 단어는 test_sentence에 누적해 다음 작업의 입력으로 활용
  print()
  print(jamotools.join_jamos(test_sentence)) # 자모 단위로 결합
  print()

# epoch이 끝날 때 마다 testmodelFunc 호출해 진행 결과를 출력
# fit 할 때(학습 도중) 학습 데이터가 predict 되는 과정을 확인해 가며 작업하고 싶을 때 사용
testModelCb = tf.keras.callbacks.LambdaCallback(on_epoch_end=testmodelFunc)

# repeat() : input을 반복. 1개의 epoch의 끝과 다음 epoch의 시작에 상관없이 인자 만큼 반복함
history = model.fit(train_dataset.repeat(), epochs=100,
                    steps_per_epoch=steps_per_epoch, # 한 에폭에 사용할 step수를 지정. ex) 총 45개 sample이 있고 배치 사이즈가 3이라면 15step으로 지정
                    )

print(history.history['loss'][-1])
print(history.history['accuracy'][-1])

model.save('tfc_33model.hdf5')

from keras.models import load_model
model = load_model('tfc_33model.hdf5')

# 임의 문장을 사용해 생성된 새로운 문장 확인
test_sentence = '이날은 수수개비를 꺾어도 아이들은 매를 맞지 않는다'
test_sentence = jamotools.split_syllables(test_sentence)

next_chars = 500
for _ in range(next_chars):
    test_text_x = test_sentence[-seq_length:]  # 임의의 문장 뒤에서 부터 seq_length(25) 만큼 선택
    test_text_x = np.array([char2idx[c] if c in char2idx else char2idx['UNK'] for c in test_text_x])
    test_text_x = pad_sequences([test_text_x], maxlen=seq_length, padding='pre', value=char2idx['UNK'])
    output_idx = np.argmax(model.predict(test_text_x)[0])  # 출력값 중에서 가장 값이 큰 인덱스 반환
    test_sentence += idx2char[output_idx]  # 출력 단어는 test_sentence에 누적해 다음 작업의 입력으로 활용

print(jamotools.join_jamos(test_sentence))  # 자모 단위로 결합

