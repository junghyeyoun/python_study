# 1) step1 : array 관련 문제
# 정규분포를 따르는 난수를 이용하여 5행 4열 구조의 다차원 배열 객체를 생성하고, 각 행 단위로 합계, 최댓값을 구하시오.

import numpy as np

# 5행 4열의 정규분포를 따르는 난수로 채워진 배열 생성
array = np.random.normal(0, 1, size=(5, 4))

# 각 행 단위로 합계 계산
row_sums = np.sum(array, axis=1)

# 각 행 단위로 최댓값 계산
row_max = np.max(array, axis=1)

print("다차원 배열:")
print(array)

print("각 행의 합계:")
print(row_sums)

print("각 행의 최댓값:")
print(row_max)

# 2) step2 : indexing 관련문제
# 문2-1) 6행 6열의 다차원 zero 행렬 객체를 생성한 후 다음과 같이 indexing 하시오.
# 조건1> 36개의 셀에 1~36까지 정수 채우기
# 조건2> 2번째 행 전체 원소 출력하기  => 출력 결과 : [ 7.   8.   9.  10.  11.  12.]
# 조건3> 5번째 열 전체 원소 출력하기 =>  출력결과 : [ 5. 11. 17. 23. 29. 35.]
# 조건4> 15~29 까지 아래 처럼 출력하기 => 15~29, 3행 3열, 2차원 배열

# 6행 6열의 zero 행렬 생성
matrix = np.zeros((6, 6))

# 1부터 36까지의 정수를 6x6 행렬에 채우기
matrix[0:6, 0:6] = np.arange(1, 37).reshape(6, 6)

# 2번째 행 전체 원소 출력
row2 = matrix[1, :]
print("2번째 행 전체 원소 출력:")
print(row2)

# 5번째 열 전체 원소 출력
col5 = matrix[:, 4]
print("5번째 열 전체 원소 출력:")
print(col5)

# 15~29까지의 부분 행렬 출력
sub_matrix = matrix[2:5, 2:5]
print("15~29까지의 부분 행렬 출력:")
print(sub_matrix)

# 문2-2) 6행 4열의 다차원 zero 행렬 객체를 생성한 후 아래와 같이 처리하시오.
# 조건1> 20~100 사이의 난수 정수를 6개 발생시켜 각 행의 시작열에 난수 정수를 저장하고, 두 번째 열부터는 1씩 증가시켜 원소 저장하기
# 조건2> 첫 번째 행에 1000, 마지막 행에 6000으로 요소값 수정하기
# <<출력 예시>>
# 1. zero 다차원 배열 객체
# 2. 난수 정수 발생
# 3. zero 다차원 배열에 난수 정수 초기화 결과. 두 번째 열부터는 1씩 증가시켜 원소 저장하기
# 4. 첫 번째 행에 1000, 마지막 행에 6000으로 수정
import numpy as np
import random

# 6행 4열의 zero 행렬 생성
matrix = np.zeros((6, 4))

# 20~100 사이의 난수 정수를 6개 발생시켜 각 행의 시작열에 저장하고, 두 번째 열부터는 1씩 증가시켜 원소 저장
for i in range(6):
    start_value = random.randint(20, 100)
    matrix[i, 0] = start_value
    for j in range(1, 4):
        matrix[i, j] = start_value + j

# 첫 번째 행에 1000, 마지막 행에 6000으로 요소값 수정
matrix[0, :] = 1000
matrix[5, :] = 6000

# 결과 출력
print("zero 다차원 배열 객체 : ")
print(matrix)

# 3) step3 : unifunc 관련문제
# 표준정규분포를 따르는 난수를 이용하여 4행 5열 구조의 다차원 배열을 생성한 후
# 아래와 같이 넘파이 내장함수(유니버설 함수)를 이용하여 기술통계량을 구하시오.
# 배열 요소의 누적합을 출력하시오.
import numpy as np

# 4행 5열의 표준정규분포 난수로 채워진 다차원 배열 생성
array = np.random.randn(4, 5)

# 배열 출력
print("4행 5열 다차원 배열:")
print(array)

# 평균, 합계, 표준편차, 분산, 최댓값, 최솟값 계산 및 출력
mean = np.mean(array)
sum_ = np.sum(array)
std_dev = np.std(array)
variance = np.var(array)
max_value = np.max(array)
min_value = np.min(array)

print("\n출력 결과:")
print("평균:", mean)
print("합계:", sum_)
print("표준편차:", std_dev)
print("분산:", variance)
print("최댓값:", max_value)
print("최솟값:", min_value)

# 1사분위 수, 2사분위 수, 3사분위 수 계산
q1 = np.percentile(array, 25)
q2 = np.percentile(array, 50)
q3 = np.percentile(array, 75)

print("1사분위 수:", q1)
print("2사분위 수:", q2)
print("3사분위 수:", q3)

# 요소값 누적합 계산
cumulative_sum = np.cumsum(array)
print("요소값 누적합:")
print(cumulative_sum)

