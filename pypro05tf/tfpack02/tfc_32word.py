# -*- coding: utf-8 -*-
"""tfc_32word.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13YxpWxUH3-rlPs1xLx-1OqPUnSdLF28f
"""

import keras
import numpy as np

path = keras.utils.get_file(
    'rnn_short_toji.txt',
    origin='https://raw.githubusercontent.com/pykwon/etc/master/rnn_test_toji.txt')
text = open(path, 'rb').read().decode(encoding='utf-8')

print('전체 글자 수 : {}'.format(len(text)))
print(text[:100])

# 데이터 정제
import re

def clean_str_func(string):
  string = re.sub(r"[^가-힣0-9(), ?!]","",string)
  string = re.sub(r"!","! ",string)
  string = re.sub(r"\(","",string)
  string = re.sub(r"\)","",string)
  string = re.sub(r"\?","? ",string)
  string = re.sub(r"\s{2,}"," ",string) # 공백 두개 이상이면 공백 하나로 바꾸기
  string = re.sub(r"\'","",string)
  return string

# print(clean_str_func("abc,,?! AB 12 나는 '  (간다) 34"))

train_text = text.split('\n')
train_text = [clean_str_func(sentence) for sentence in train_text]
print(train_text[:5])

train_text_x = []
for sen in train_text:
  train_text_x.extend(sen.split(' '))
  train_text_x.append('\n')

train_text_x = [word for word in train_text_x if word != ''] # 단어1 단어2 단어3 -> 공백을 기준으로 단어를 나눔
print(train_text_x[:5])
# train_text_y = []

# 단어 사전
vocab = sorted(set(train_text_x))
vocab.append('UNK') # 단어 사전에 존재하지 않는 토큰은 'UNK'로 처리
# 특수 토근 <unk> 토크나이저가 모르는 단어를 만나면 unknown으로 처리하기 위한 처리용 토큰입니다.
# <eos>, <pad> ,<sep>, <mask>
print('{}unique words'.format(len(vocab))) # token(word) : 54048개
print(train_text_x[:20])

# 단어 인덱싱
word2idx = {w: i for i, w in enumerate(vocab)}
# print(word2idx)
idx2word = np.array(vocab)
print(idx2word) # ['\n' ',' ',,?' ... '힘찼으며' '힝' 'UNK']
text_as_int = np.array([word2idx[c] for c in train_text_x])
print(text_as_int) # [43654     6 50166 ... 40598     0     0]

print(train_text_x[:20])
print(text_as_int[:20])

# dataset 작성
seq_length = 25 # 25개의 단어가 주어질 경우 다음 단어를 예측
example_per_epoch = len(text_as_int) // seq_length
print(example_per_epoch)

import tensorflow as tf
sentence_dataset = tf.data.Dataset.from_tensor_slices(text_as_int) # 전체가 아니라 부분 데이터 읽기
sentence_dataset = sentence_dataset.batch(seq_length + 1, drop_remainder=True)
# seq_length + 1 : 처음 25개 단어와 그 뒤에 나오는 정답(label)이 될 한 단어를 합쳐 반환하기 위함
# drop_remainder=True : 마지막 배치 크기를 무시

for item in sentence_dataset.take(1): # batch를 한번씩 불러옴 -> 데이터가 양이 많을 때 이렇게 불러옴(청크처럼)
  print(item.numpy())
  print(idx2word[item.numpy()])

def split_input_target(chunk):
  return [chunk[:-1],chunk[-1]] # [25단어].1단어

train_dataset = sentence_dataset.map(split_input_target)

for x, y in train_dataset.take(1):
  print(idx2word[x.numpy()])
  print(x.numpy())
  print(idx2word[y.numpy()])
  print(y.numpy())

# model
BATCH_SIZE = 64
steps_per_epoch = example_per_epoch // BATCH_SIZE
BUFFER_SIZE = 5000

# suffle을 사용하면 epoch마다 Dataset을 섞을 수 있다.
train_dataset = train_dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

total_words = len(vocab)
print(total_words) # 54048

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(total_words, 100, input_length=seq_length),
    tf.keras.layers.LSTM(units=256, return_sequences=True),
    tf.keras.layers.Dropout(rate=0.2),
    tf.keras.layers.LSTM(units=256),
    tf.keras.layers.Dense(units=total_words, activation='relu'),
    tf.keras.layers.Dense(units=total_words, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print(model.summary())

# 단어 단위 생성 모델 학습
from keras.preprocessing.sequence import pad_sequences

def testmodelFunc(epoch, logs):
  if epoch % 5 != 0 and epoch != 49: # 5의 배수이거나 49이면 처리
    return

  test_sentence = train_text[0]

  next_words = 100
  for _ in range(next_words):
    test_text_x = test_sentence.split(' ')[seq_length:] # 임의의 문장 뒤에서 부터 seq_length(25) 만큼 선택
    test_text_x = np.array(word2idx[c] if c in word2idx else word2idx['UNK'] for c in test_text_x)
    test_text_x = pad_sequences([test_text_x], maxlen=seq_length, padding='pre', value=word2idx['UNK'])
    ouput_idx = np.argmax(model.predict(test_text_x)[0]) # 출력 값 중에서 가장 값이 큰 인덱스 반환
    test_sentence += ' ' + idx2word[ouput_idx[0]] # 출력 단어는 test_sentence에 누적해 다음 작업의 입력으로 활용
  print()
  print(test_sentence)
  print()

# epoch이 끝날 때 마다 testmodelFunc 호출해 진행 결과를 출력
# fit 할 때(학습 도중) 학습 데이터가 predict 되는 과정을 확인해 가며 작업하고 싶을 때 사용
testModelCb = tf.keras.callbacks.LambdaCallback(on_epoch_end=testmodelFunc)

# repeat() : input을 반복. 1개의 epoch의 끝과 다음 epoch의 시작에 상관없이 인자 만큼 반복함
history = model.fit(train_dataset.repeat(), epochs=50,
                    steps_per_epoch=steps_per_epoch, # 한 에폭에 사용할 step수를 지정. ex) 총 45개 sample이 있고 배치 사이즈가 3이라면 15step으로 지정
                    )

print(history.history['loss'][-1])
print(history.history['accuracy'][-1])

model.save('tfc_32model.hdf5')

from keras.model import load_model
model = load_model('tfc_32model.hdf5')

# 임의 문장을 사용해 생성된 새로운 문장 확인
test_sentence = '이날은 수수개비를 꺾어도 아이들은 매를 맞지 않는다'

next_words = 100
for _ in range(next_words):
    test_text_x = test_sentence.split(' ')[seq_length:] # 임의의 문장 뒤에서 부터 seq_length(25) 만큼 선택
    test_text_x = np.array(word2idx[c] if c in word2idx else word2idx['UNK'] for c in test_text_x)
    test_text_x = pad_sequences([test_text_x], maxlen=seq_length, padding='pre', value=word2idx['UNK'])
    ouput_idx = np.argmax(model.predict(test_text_x)[0]) # 출력 값 중에서 가장 값이 큰 인덱스 반환
    test_sentence += ' ' + idx2word[ouput_idx[0]] # 출력 단어는 test_sentence에 누적해 다음 작업의 입력으로 활용
print()
print(test_sentence)