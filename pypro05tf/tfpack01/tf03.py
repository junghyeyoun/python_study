# tf.constant() : 탠서를 직접 기억
# tf.Variable() : 탠서가 저장된 주소를 참조

import tensorflow as tf  
import numpy as np 
from astropy.io.tests.mixin_columns import su

node1 = tf.constant(3, dtype=tf.float32)
node2 = tf.constant(4.0) # 기본이 float32
print(node1)
print(node2)
imsi = tf.add(node1, node2)
print(imsi)

print()
node3 = tf.Variable(3, dtype=tf.float32)
node4 = tf.Variable(4.0)
print(node3)
print(node4)
node4.assign_add(node3)
print(node4)

print()
a = tf.constant(5)
b = tf.constant(10)
c = tf.multiply(a, b)
result = tf.cond(a < b, lambda : tf.add(10,c), lambda : tf.square(a))
print('result : ',result.numpy())

print('---------')
v = tf.Variable(1)

@tf.function # Graph 환경에서 처리가 됨
def find_next_func():
    v.assign(v+1)
    if tf.equal(v % 2, 0):
        v.assign(v + 10)
        
find_next_func()
print(v.numpy())
print(type(find_next_func))
# <class 'function'> - @tf.function 쓰면 -> <class 'tensorflow.python.eager.polymorphic_function.polymorphic_function.Function'>
# 일반 함수에서 텐서영역에서 사용하는 함수로 바뀜

print('func1 -----------------------------')
def func1():
    imsi = tf.constant(0)   # imsi = 0
    su = 1
    for _ in range(3):
        imsi = tf.add(imsi, su)
    return imsi

kbs = func1()
print(kbs.numpy(), ' ', np.array(kbs)) # 둘다 똑같은거임

print('func2 -----------------------------')
imsi = tf.constant(0)
@tf.function # 그래프 영역내에서 수행
def func2():
    #imsi = tf.constant(0)   # imsi = 0
    global imsi # 함수 밖에서 변수가 선언된 경우
    su = 1
    for _ in range(3):
        #imsi = tf.add(imsi, su)
        #imsi = imsi + su
        imsi += su
    return imsi

kbs = func2()
print(kbs.numpy(), ' ', np.array(kbs)) 

print('func3 -----------------------------')
imsi = tf.Variable(0)
@tf.function
def func3():
    #imsi = tf.Variable(0)  # autograph에서는 Variable()은 함수 밖에서 선언해야함
    su = 1
    for _ in range(3):
        imsi.assign_add(su)
        # imsi = imsi + su  # err
        # imsi += su # err
    return imsi

kbs = func3()
print(kbs.numpy(), ' ', np.array(kbs)) 

print('구구단 출력 -----------------------------')
@tf.function 
def gugu1(dan):
    su = 0
    for _ in range(9):
        su = tf.add(su, 1)
        print(su) # good
        # print(su.numpy()) # err
        # print('{} * {} = {}'.format(dan, su, dan*su)) # 서식이 있는 출력 안됨
        
gugu1(3)

print('----------------------------------')
# 내장함수 :  일반적으로 numpy 지원함수를 그대로 사용 + 알파
# ... 중 reduce ~ 함수 : 차원을 떨어트리고 연산
ar = [[1.,2.],[3.,4.]] # 뒤에 점하나 찍어주면 실수 연산
print(tf.reduce_sum(ar).numpy()) # 차원을 떨어트리고 전체 합 구함
print(tf.reduce_mean(ar, axis=0).numpy()) # 열 기준 차원 떨어트리고 평균
print(tf.reduce_mean(ar, axis=1).numpy()) # 행 기준 차원 떨어트리고 평균
# cost를 최소화

# one_hot encoding : 주로 종속변수 범주형 데이터일때 사용
print(tf.one_hot([0,1,2,0], depth=3)) # depth 자리수 확보

