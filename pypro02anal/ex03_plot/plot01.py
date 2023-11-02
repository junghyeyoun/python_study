# 시각화 
import numpy as np 
import matplotlib.pyplot as plt
plt.rc('font',family='malgun gothic')
plt.rcParams['axes.unicode_minus'] =False # 한글처리할 때 음수 쓰면 깨지는 현상 해결
'''
# x = {'서울','수원' ,'인천'} # set은 안됨 ->  순서가 없고 유니크하기 때문에 
# x = ['서울','수원' ,'인천'] # list
x = ('서울','수원' ,'인천') # tuple
y = [5,3,7]
plt.xlim([-1,3])
plt.ylim([-3,10])
plt.plot(x,y)
plt.yticks(list(range(-3,11,3))) # -3부터 10까지 증가치는 3
plt.xlabel('지역명')
plt.ylabel('친구수')
plt.title('선 그래프')
plt.show()
'''
'''
#sin 곡선
x = np.arange(10)
y = np.sin(x)
print(x,y)
# plt.plot(x,y,'bo') # 파란점 산포도 같이 나타냄
plt.plot(x,y,'go--',linewidth=3, markersize=10 ) # 초록색 점 사이 파선 나타냄
plt.show()
'''
# hold : 복수의 차트 그리기 명령을 하나의 figure에 표현할 수 있다.
x = np.arange(0, np.pi*3, 0.1)
# print(x)
y_sin = np.sin(x)
y_cos = np.cos(x)
'''

plt.figure(figsize=(10,5)) # 창(영역) 사이즈
plt.plot(x, y_sin, c='r') # 직선
plt.scatter(x, y_cos, c='b') # 산점도
plt.legend(['sine','cosine'],loc=3) # loc 시계 반대방향으로 감 / 10주면 가운데
plt.show()
'''

# subplot : figure를 여러 개의 영역으로 나눠 차트를 그림
plt.subplot(2,1,1)
plt.plot(x,y_sin)
plt.title('sine')
plt.subplot(2,1,2)
plt.plot(x,y_cos)
plt.title('cosine')
plt.show()