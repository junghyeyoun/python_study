# cost와 accuracy(정확도)/r2score(설명력)은 반비례한다.
import numpy as np 
import math 

# 모델 학습이 끝나고 예측 값 구하기 단계에 있다고 가정
real = np.array([10, 9, 3, 2, 11])
#pred = np.array([11, 5, 2, 4, 3]) # 실제값과 차이가 적음  17.2
pred = np.array([15, 8, 2, 9, 2]) # 실제값과 차이가 큼  31.4
cost = 0 
for i in range(5):
    cost += math.pow(pred[i] - real[i], 2)
    print(cost)
    
print('\n',cost / len(pred))

print('---------------------------------------------------------')
import tensorflow as tf 
import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
b = 0
# tensorflow에서 cost minimize하는 방법
# hypothesis = w*x +b
# cost = tf.reduce_sum(tf.pow(hypothesis - y, 2)) / len(x)
# cost = tf.reduce_mean(tf.pow(hypothesis - y, 2)) 

w_val = []
cost_val = []

# 가중치 만들기
for i in range(-30, 50):
    feed_w = i * 0.1
    hypothesis = tf.multiply(feed_w, x) + b  # = w*x +b
    cost = tf.reduce_mean(tf.square(hypothesis - y))  # Calculate cost
    cost_val.append(cost)
    w_val.append(feed_w)
    print(str(i) + ' 번 수행 ' + ', cost : ' + str(cost.numpy()) + ', weight : ' + str(feed_w))
    
plt.plot(w_val, cost_val)
plt.xlabel('w')
plt.ylabel('cost')  # Fixed typo here, changed 'xlabel' to 'ylabel'
plt.show()