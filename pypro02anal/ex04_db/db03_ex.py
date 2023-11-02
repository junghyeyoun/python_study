import MySQLdb
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font',family='malgun gothic')
plt.rcParams['axes.unicode_minus'] =False
import seaborn as sns
import sys
import csv

# a) MariaDB에 저장된 jikwon, buser, gogek 테이블을 이용하여 아래의 문제에 답하시오.
# - 사번 이름 부서명 연봉, 직급을 읽어 DataFrame을 작성
# - DataFrame의 자료를 파일로 저장
# - 부서명별 연봉의 합, 연봉의 최대/최소값을 출력
# - 부서명, 직급으로 교차 테이블(빈도표)을 작성(crosstab(부서, 직급))
# - 직원별 담당 고객자료(고객번호, 고객명, 고객전화)를 출력. 담당 고객이 없으면 "담당 고객  X"으로 표시
# - 부서명별 연봉의 평균으로 가로 막대 그래프를 작성
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
        select jikwon_no, jikwon_name, buser_name, jikwon_pay ,jikwon_jik 
        from jikwon inner join buser on buser_num = buser_no
    '''
    cursor.execute(sql)
    
    # DataFrame 작성
    df = pd.DataFrame(cursor.fetchall(), columns=['사번', '이름', '부서명', '연봉', '직급'])
    print(df.head(3))
    
    # DataFrame의 자료를 파일로 저장
    with open('jikdata_ex.csv',mode='w',encoding='utf-8') as fobj:
        writer = csv.writer(fobj)
        for r in cursor:
            writer.writerow(r)
            
    # 부서별 연봉의 합
    grouped = df.groupby('부서명')['연봉'].sum()
    print('\n부서별 연봉의 합:')
    print(grouped)
    
    # 연봉 최대, 최소값
    print('연봉 최대값 : ',df['연봉'].max())
    print('연봉 최대값 : ',df['연봉'].min())
    
    # 부서명, 직급 교차 테이블(빈도표)
    ctab = pd.crosstab(df['부서명'],df['직급'],margins=True)
    print('\n교차표')
    print(ctab)
    
    # 직원별 담당 고객자료
    sql2 = '''
        select jikwon_name, gogek_no, gogek_name, gogek_tel 
        from jikwon left outer join gogek on jikwon_no = gogek_damsano
    '''
    df2 = pd.read_sql(sql2, conn)
    df2.columns = ['직원이름','고객번호', '고객명', '고객전화']
    df2.fillna("담당 고객 X", inplace=True)
    print(df2)
    
    # 시각화
    jik_mpay = df.groupby(['부서명'])['연봉'].mean()
    # print(jik_mpay.index)
    # print(jik_mpay.values)
    plt.barh(jik_mpay.index, jik_mpay.values)
    plt.xlabel('평균 연봉')
    plt.ylabel('부서명')
    plt.title('부서별 평균 연봉')
    plt.show()

# b) MariaDB에 저장된 jikwon 테이블을 이용하여 아래의 문제에 답하시오.
# - pivot_table을 사용하여 성별 연봉의 평균을 출력
# - 성별(남, 여) 연봉의 평균으로 시각화 - 세로 막대 그래프
# - 부서명, 성별로 교차 테이블을 작성 (crosstab(부서, 성별))
    
    sql3 = '''
        select jikwon_gen, jikwon_pay, buser_name 
        from jikwon inner join buser on buser_num = buser_no
    '''
    cursor.execute(sql3)
    df3 = pd.DataFrame(cursor.fetchall(), columns=['성별', '연봉', '부서명'])
    # print(df3.head(3),len(df3))
    print()
    
    # pivot_table : 성별 연봉의 평균
    pivot_table = pd.pivot_table(df3, values='연봉', index='성별', aggfunc=np.mean)
    print(pivot_table)

    # 시각화 
    jik_gpay = df3.groupby(['성별'])['연봉'].mean()
    print(jik_gpay.index)
    print(jik_gpay.values)
    plt.bar(jik_gpay.index, jik_gpay.values)
    plt.xlabel('평균 연봉')
    plt.ylabel('부서명')
    plt.title('부서별 평균 연봉')
    plt.show()
    
    # 교차표
    ctab2 = pd.crosstab(df3['부서명'],df3['성별'],margins=True)
    print('\n교차표')
    print(ctab2)

except Exception as e:
    print('처리 오류 : ',e)
finally:
    cursor.close()
    conn.close()
 
 
