import pandas as pd
from pandas import DataFrame,Series
import numpy as np

print('문제 1')
print('a) 표준정규분포를 따르는 9 X 4 형태의 DataFrame을 생성하시오.')
print('b) a에서 생성한 DataFrame의 칼럼 이름을 - No1, No2, No3, No4로 지정하시오')
ex1 = DataFrame(np.random.randn(9, 4), columns=['No1','No2','No3','No4'])
print(ex1)
print('\nc) 각 컬럼의 평균을 구하시오. mean() 함수와 axis 속성 사용')
print(ex1.mean(axis=0))

print('\n\n문제 2')
print('a) DataFrame으로 위와 같은 자료를 만드시오. colume(열) name은 numbers, row(행) name은 a~d이고 값은 10~40.')
ex2 = DataFrame([10,20,30,40], index=['a','b','c','d'], columns=['numbers'])
print(ex2,'\n')

print('b) c row의 값을 가져오시오.')
print(ex2.loc['c'],'\n')

print('c) a, d row들의 값을 가져오시오.')
print(ex2.loc[['a','d']],'\n')

print('d) numbers의 합을 구하시오.')
print(ex2['numbers'].sum(),"\n")

print('e) numbers의 값들을 각각 제곱하시오. 아래 결과가 나와야 함.')
print(ex2.mul(ex2),'\n')

print('f) floats 라는 이름의 칼럼을 추가하시오. 값은 1.5, 2.5, 3.5, 4.5    아래 결과가 나와야 함.')
ex2['floats']=[1.5,2.5,3.5,4.5]
print(ex2,'\n')

print('g) names라는 이름의 다음과 같은 칼럼을 위의 결과에 또 추가하시오. Series 클래스 사용.')
exg = Series(['길동', '오정', '팔계','오공'], index=['d','a','b', 'c'])
ex2['name'] = exg
print(ex2,'\n')
print(ex2.reindex(['d','a','b','c']))
