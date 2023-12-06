# 글자 수준의 LSTM 텍스트 생성 모델 구현 - 니체의 글을 사용
import keras
import numpy as np

# path = keras.utils.get_file(
#     'nietzsche.txt',
#     origin='https://s3.amazonaws.com/text-datasets/nietzsche.txt')
# text = open(path).read().lower()

path = keras.utils.get_file(
    'rnn_short_toji.txt',
    origin='https://raw.githubusercontent.com/pykwon/etc/master/rnn_short_toji.txt')
text = open(path, encoding='utf-8').read().lower()

print('말뭉치 크기(행 수):', len(text))

import re
text = re.sub('[^가-힣 ]','',text)
print(set(text))
chars = sorted(list(set(text)))
print(chars)
print('사용 가능한 문자 수 : ',len(chars))

char_index = dict((c, i) for i, c in enumerate(chars))
index_char = dict((i, c) for i, c in enumerate(chars))
print('char_index : ',char_index)
print('index_char : ',index_char)


# 60개 글자로 된 시퀀스를 추출합니다.
maxlen = 30 

# 한 글자씩 건너 뛰면서 새로운 시퀀스를 샘플링합니다.
step = 1

# 추출한 시퀀스를 담을 리스트
sentences = []

# 타깃(시퀀스 다음 글자)을 담을 리스트
next_chars = []

for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])
print('시퀀스 개수:', len(sentences))

# 말뭉치에서 고유한 글자를 담은 리스트
chars = sorted(list(set(text)))
print('고유한 글자:', len(chars))

# chars 리스트에 있는 글자와 글자의 인덱스를 매핑한 딕셔너리
char_indices = dict((char, chars.index(char)) for char in chars)

# 글자를 원-핫 인코딩하여 0과 1의 이진 배열로 바꿉니다.
print('벡터화...')
x = np.zeros((len(sentences), maxlen, len(chars)), dtype=bool)
y = np.zeros((len(sentences), len(chars)), dtype=bool)
for i, sentence in enumerate(sentences): 
    for t, char in enumerate(sentence):
        x[i, t, char_indices[char]] = 1  # x [면, 행, 열]=1
        y[i, char_indices[next_chars[i]]] = 1 # y[행,열]=1

# 네트워크 구성
# 이 네트워크는 하나의 LSTM 층과 그 뒤에 Dense 분류기가 뒤따릅니다. 분류기는 가능한 모든 글자에 대한 소프트맥스 출력을 만듭니다. 
#순환 신경망이 시퀀스 데이터를 생성하는 유일한 방법은 아닙니다. 최근에는 1D 컨브넷도 이런 작업에 아주 잘 들어 맞는다는 것이 밝혀졌습니다.
from keras.layers import LSTM, Dense

model = keras.models.Sequential()
model.add(LSTM(128, input_shape=(maxlen, len(chars)), activation='tanh'))
model.add(Dense(len(chars), activation='softmax'))

optimizer = keras.optimizers.RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)
print(model.summary())

# softmax 함수를 수식을 이용해 작성
def sample(preds, temperature=1.0): # temperature로 확률 분포의 가중치를 조정
    # array() : 원본 생성시 복사본은 변경 안됨. asarray() : 원본 생성시 복사본도 변경함.
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature # log : 큰 수를 작게 만들고(비율) 복작합 계산을 단순화
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

import random
import sys

random.seed(42)
start_index = random.randint(0, len(text) - maxlen - 1)

# 60 에포크 동안 모델을 훈련합니다
for epoch in range(1, 6): # 편의상 5 에폭 동안 모델 훈련
    print('에포크', epoch)
    # 데이터에서 한 번만 반복해서 모델을 학습합니다
    model.fit(x, y, batch_size=128, epochs=1)

    # 무작위로 시드 텍스트를 선택합니다
    seed_text = text[start_index: start_index + maxlen]
    print('--- 시드 텍스트: "' + seed_text + '"')

    # 여러가지 샘플링 온도를 시도합니다
    for temperature in [0.2, 0.5, 1.0, 1.2]:
        print('------ 온도:', temperature)
        generated_text = seed_text
        sys.stdout.write(generated_text)

        # 시드 텍스트에서 시작해서 400개의 글자를 생성합니다
        for i in range(400):
            # 지금까지 생성된 글자를 원-핫 인코딩으로 바꿉니다
            sampled = np.zeros((1, maxlen, len(chars)))
            for t, char in enumerate(generated_text):
                sampled[0, t, char_indices[char]] = 1.

            # 다음 글자를 샘플링합니다
            preds = model.predict(sampled, verbose=0)[0]
            next_index = sample(preds, temperature)
            next_char = chars[next_index]

            generated_text += next_char
            generated_text = generated_text[1:]

            sys.stdout.write(next_char)
            sys.stdout.flush()
        print()
