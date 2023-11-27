# 변수 선언 후 사용하기
# tf.Variable()

import tensorflow as tf

print(tf.constant(1.0))  # 고정된 자료를 기억

f = tf.Variable(1.0)  # 변수형 0-d 텐서 : scala
v = tf.Variable(tf.ones(2,))  # 1-d 텐서 : vector
m = tf.Variable(tf.ones(2,1))  # 2-d 텐서 : matrix
print(f)
print(v)
print(m)
print()

# 치환
v1 = tf.Variable(1)
v1.assign(10)
print('v1 :', v1, v1.numpy())

print()
w = tf.Variable(tf.ones(shape=(1,)))
b = tf.Variable(tf.ones(shape=(1,)))
w.assign([2])
b.assign([3])

def func1(x):
    return w * x + b

print(func1(3))

@tf.function  # auto graph 기능 : 별도의 텐서 영역에서 연산을 수행. tf.Graph + tf.Session
def func2(x):
    return w * x + b

print(func2(3))

print('Variable의 치환 / 누적')
aa = tf.ones(2, 1)
print(aa.numpy())
m = tf.Variable(tf.zeros(2, 1))
m.assign(aa)   # 치환
print(m.numpy())

m.assign_add(aa)
print(m.numpy())

m.assign_sub(aa)
print(m.numpy())

print('---------------')
g1 = tf.Graph()

with g1.as_default():
    c1 = tf.constant(1, name="c_one")  # c1은 'c_one'이란 이름의 정수 1을 가진 상수(고정된 값을 기억)다.
    print(c1)
    print(type(c1))
    print(c1.op)
    print('---------')
    print(g1.as_graph_def())

print('~~~~~~~~~~~~~~~')
g2 = tf.Graph()

with g2.as_default():
    v1 = tf.Variable(initial_value=1, name='v1')
    print(v1)
    print(type(v1))
    print(v1.op)
    
print(g2.as_graph_def())

