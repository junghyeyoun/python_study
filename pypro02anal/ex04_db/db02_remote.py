# 원격DB와 연동 후 자료를 읽어 DataFrame에 저장 ...
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
        select jikwon_no, jikwon_name, jikwon_jik, buser_name, jikwon_gen, jikwon_pay
        from jikwon inner join buser on buser_num = buser_no
    '''
    cursor.execute(sql)
    
    # 출력1 : console
    for a,b,c,d,e,f in cursor:
        print(a,b,c,d,e,f)
    print()
    
    # 출력2 : DataFrame
    df = pd.DataFrame(cursor.fetchall(), columns=['jikwon_no', 'jikwon_name', 'jikwon_jik', 'buser_name', 'jikwon_gen', 'jikwon_pay'])
    print(df.head(3),len(df))
    print()
    
    # 출력3 : csv파일로 저장
    with open('jikdata.csv',mode='w',encoding='utf-8') as fobj:
        writer = csv.writer(fobj)
        for r in cursor:
            writer.writerow(r)
    
    #저장된 csv파일 읽기
    df2 = pd.read_csv('jikdata.csv', header=None, names=['번호','이름','직급','부서명','성별','연봉'])
    print(df2.head(3))
    print()
    
    # 출력4 : DataFrame의 sql 사용
    df3 = pd.read_sql(sql, conn)
    df3.columns=['번호', '이름', '직급', '부서명', '성별', '연봉']
    print(df3.head(3))
    
    # DataFrame의 자료로 기술 통계 : 대표값, 요약통계량, 도수분포표, 시각화 ...
    print(df3[:3])
    print(df3[:-27])
    print('건수 : ',len(df3),df3['이름'].count())
    print('직급별 인원수 : ',df3['직급'].value_counts())
    print('연봉 평균 : ',df3.loc[:,'연봉'].mean())
    print('연봉 평균의 표준편차 : ',df3.loc[:,'연봉'].std())
    print(df3.loc[:,'연봉'].describe()) # 요약 통계량
    print(df3.loc[df2['연봉']>=7000]) # 연봉이 7000이상인 직원 출력
    # 교차표
    ctab = pd.crosstab(df3['성별'],df3['직급'],margins=True)
    print(ctab)
    print()
    print(df3.groupby(['성별','직급'])['이름'].count())
    print()
    print()
    print(df3.pivot_table(['연봉'],index=['성별','직급'],aggfunc=np.mean))
    
    # 시각화 : pie
    jik_ypay = df3.groupby(['직급'])['연봉'].mean() # 직급별 연봉 평균 / 반환값 series
    print(jik_ypay.index)
    print(jik_ypay.values)
    plt.pie(jik_ypay,labels=jik_ypay.index, shadow=True, labeldistance=0.7, counterclock=False)
    plt.show()
    
except Exception as e:
    print('처리 오류 : ',e)
finally:
    cursor.close()
    conn.close()
    