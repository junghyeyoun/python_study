from scipy import stats
import pandas as pd
import numpy as np 
import random

# [two-sample t 검정 : 문제1] 
# 다음 데이터는 동일한 상품의 포장지 색상에 따른 매출액에 대한 자료이다. 
# 포장지 색상에 따른 제품의 매출액에 차이가 존재하는지 검정하시오.

# 귀무 : 포장지 색상에 따른 제품의 매출액에 차이가 존재하지 않는다.
# 대립 : 포장지 색상에 따른 제품의 매출액에 차이가 존재한다.

blue = [70, 68, 82, 78, 72, 68, 67, 68, 88, 60, 80]
red = [60, 65, 55, 58, 67, 59, 61, 68, 77, 66, 66]

print(np.mean(blue),np.mean(red)) # 72.81818181818181 63.81818181818182
 
print('\n정규성 확인') 
print(stats.shapiro(blue).pvalue) 
print(stats.shapiro(red).pvalue)

print('\n등분산성 확인') 
print(stats.levene(blue, red).pvalue) 

result = stats.ttest_ind(blue, red)
print('\nt-value : %.5f, p-value : %.5f'%result)

# 판정 : p-value -> 0.00832 < 0.05 이므로, 귀무 기각.
# 따라서 포장지 색상에 따른 제품의 매출액에 차이가 존재한다.

print('\n-----------------------------------------------------------')

# [two-sample t 검정 : 문제2]  
# 아래와 같은 자료 중에서 남자와 여자를 각각 15명씩 무작위로 비복원 추출하여 혈관 내의 콜레스테롤 양에 차이가 있는지를 검정하시오.

# 귀무 : 혈관 내의 콜레스테롤 양에 차이가 없다.
# 대립 : 혈관 내의 콜레스테롤 양에 차이가 있다.

male = [0.9, 2.2, 1.6, 2.8, 4.2, 3.7, 2.6, 2.9, 3.3, 1.2, 3.2, 2.7, 3.8, 4.5, 4, 2.2, 0.8, 0.5, 0.3, 5.3, 5.7, 2.3, 9.8]
female = [1.4, 2.7, 2.1, 1.8, 3.3, 3.2, 1.6, 1.9, 2.3, 2.5, 2.3, 1.4, 2.6, 3.5, 2.1, 6.6, 7.7, 8.8, 6.6, 6.4]

random.seed(1)  
male_sample = random.sample(male, 15)
female_sample = random.sample(female, 15)
print(np.mean(male_sample),np.mean(female_sample)) # 2.453333333333333 3.6600000000000006

print('\n정규성 확인') 
print(stats.shapiro(male_sample).pvalue) 
print(stats.shapiro(female_sample).pvalue)

print('\n등분산성 확인') 
print(stats.levene(male_sample, female_sample).pvalue) 


result1 = stats.wilcoxon(male_sample, female_sample)
print('\nt-value : %.5f, p-value : %.5f'%result1)
# pvalue-> 0.09775 > 0.05 이므로 귀무 채택
# 혈관 내의 콜레스테롤 양에 차이가 없다.

print('\n-----------------------------------------------------------')

# [two-sample t 검정 : 문제3]
# DB에 저장된 jikwon 테이블에서 총무부, 영업부 직원의 연봉의 평균에 차이가 존재하는지 검정하시오.
# 연봉이 없는 직원은 해당 부서의 평균연봉으로 채워준다.

# 귀무 : 총무부, 영업부 직원의 연봉의 평균에 차이가 없다.
# 대립 : 총무부, 영업부 직원의 연봉의 평균에 차이가 있다.

import MySQLdb
import pickle
import sys

# 데이터 불러오기 
try:
    with open('mydb.dat', mode='rb') as obj:
        config = pickle.load(obj)
except Exception as e:
    print('읽기 오류 : ',e)
    sys.exit()
    
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    sql = '''
        select buser_name, jikwon_pay from jikwon right outer join buser
        on buser_num = buser_no
    '''
    cursor.execute(sql)
    data2 = pd.DataFrame(cursor.fetchall(), columns=['buser_name', 'jikwon_pay'])
    # print(data2)
    
except Exception as e:
    print('처리 오류 : ',e)
finally:
    cursor.close()
    conn.close()
    
buser1 = data2[data2['buser_name']=='총무부']
buser2 = data2[data2['buser_name']=='영업부']

pay1 = buser1['jikwon_pay']
pay2 = buser2['jikwon_pay']

print('\n정규성 확인') 
print(stats.shapiro(pay1).pvalue) 
print(stats.shapiro(pay2).pvalue)

print('\n등분산성 확인') 
print(stats.levene(pay1, pay2).pvalue) 

print(np.mean(pay1),np.mean(pay2)) # 5414.285714285715 4908.333333333333

result2 = stats.mannwhitneyu(pay1, pay2)  
print('\nt-value : %.5f, p-value : %.5f'%result2)

# 판정 : p-value -> 0.65239 > 0.05 귀무 채택
# 따라서 총무부, 영업부 직원의 연봉의 평균에 차이가 있다.


print('\n-----------------------------------------------------------')

# [대응표본 t 검정 : 문제4]
# 어느 학급의 교사는 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되고 있다고 말하고 있다.
# 이 때, 올해의 해당 학급의 중간고사 성적과 기말고사 성적은 다음과 같다. 점수는 학생 번호 순으로 배열되어 있다.
# 그렇다면 이 학급의 학업능력이 변화했다고 이야기 할 수 있는가?

# 귀무 : 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지된다.
# 대립 : 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지되지 않는다.

mid = [80, 75, 85, 50, 60, 75, 45, 70, 90, 95, 85, 80]
final = [90, 70, 90, 65, 80, 85, 65, 75, 80, 90, 95, 95]

print(np.mean(mid),np.mean(final)) # 74.16666666666667 81.66666666666667

print('\n정규성 확인') 
print(stats.shapiro(mid).pvalue) # 0.368144154548645 > 0.05
print(stats.shapiro(final).pvalue) # 0.19300280511379242 > 0.05

print('\n등분산성 확인') 
print(stats.levene(mid, final).pvalue) #0.19300280511379242 > 0.05

result3 = stats.ttest_rel(mid, final)
print('\nt-value : %.5f, p-value : %.5f'%result3)

# 판정 : p-value -> 0.18463 > 0.05이므로 귀무 채택.
# 따라서 매년 학기 내 치뤄지는 시험성적의 결과가 실력의 차이없이 비슷하게 유지된다.