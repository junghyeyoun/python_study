# 인공신경망(Artificail Neural Network, ANN)은 사람의 뇌 속 뉴런의 작용을 본떠 패턴을 구성한 컴퓨팅 시스템의 일종이다.
# 퍼셉트론(Perceptron)은 가장 단순한 유형의 인공 신경망이다. 이런 유형의 네트워크는 대게 이진법 예측을 하는데 쓰인다.
# 퍼셉트론(단층신경망, 뉴런, 노드)은 데이터를 선형적(wa+b)으로 분리할 수 있는 경우에만 효과가 있다.

import numpy as np 
from sklearn.linear_model import Perceptron 
from sklearn.metrics import accuracy_score 

feature = np.array([[0,0],[0,1],[1,0],[1,1]])
print(feature)
#label = np.array([0,0,0,1]) # and
#label = np.array([0,1,1,1]) #or
label = np.array([0,1,1,0]) #xor -> 학습횟수 높여도 정확도 0.5 => Perceptron의 맹점

m1 = Perceptron(max_iter=10000, eta0=0.1, random_state=0).fit(feature, label)  # max_iter : 학습 반복횟수, eta0 : learning rate
print(m1)
pred = m1.predict(feature)
print('pred : ',pred)
print('acc : ',accuracy_score(label, pred))

print('\n 다층 신경망 : MLP') # xor 연산 가능
from sklearn.neural_network import MLPClassifier 
m2 = MLPClassifier(hidden_layer_sizes=(30), solver='adam', learning_rate_init=0.01, verbose=1).fit(feature, label)
print(m2)
pred2 = m2.predict(feature)
print('pred2 : ',pred2)
print('acc : ',accuracy_score(label, pred2))