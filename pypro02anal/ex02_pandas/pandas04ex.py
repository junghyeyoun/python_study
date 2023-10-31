# 문제 3번
import pandas as pd 

df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/titanic_data.csv')  
print(df)

#  1) 데이터프레임의 자료로 나이대(소년, 청년, 장년, 노년)에 대한 생존자수를 계산한다.

df['Age_Group'] = pd.cut(df['Age'],bins=[1,20,35,60,150],labels=['소년','청년','장년','노년'])
print(df)

survived_by_age_group = df.groupby('Age_Group')['Survived'].value_counts()
print(survived_by_age_group)

# 2) 성별 및 선실에 대한 자료를 이용해서 생존여부(Survived)에 대한 생존율을 피봇테이블 형태로 작성한다. 
# index에는 성별(Sex)를 사용하고, column에는 선실(Pclass) 인덱스를 사용한다.
pivot_result = df.pivot_table(values=['Survived'], index=['Sex','Age_Group'],columns=['Pclass'],aggfunc='mean')*100
pivot_result = pivot_result.round(2)

print(pivot_result)

# 문제 4번
print('\n\n-------------------------------------')
# 1)  human.csv 파일을 읽어 아래와 같이 처리하시오.
# - Group이 NA인 행은 삭제
# - Career, Score 칼럼을 추출하여 데이터프레임을 작성
# - Career, Score 칼럼의 평균계산
df2 = pd.read_csv('../testdata/human.csv')
print(df2)
df2.columns = df2.columns.str.strip() # 공백제거
print(df2)
df2 = df2[df2['Group'].str.strip() != 'NA'] # Group인 NA인 행 삭제
print(df2)
df2 = df2[['Career', 'Score']] # Career, Score 칼럼을 추출하여 DataFrame 을 작성
print(df2)
# avg_career = df['Career'].mean()
avg_score = df2['Score'].mean()
avg_career = df2['Career'].mean()
avg_score = df2['Score'].mean()
print()
# 결과 출력
print(df2)
print(f'평균 Career: {avg_career}')
print(f'평균 Score: {avg_score}')
print(df2.mean())

#2) tips.csv 파일을 읽어 아래와 같이 처리하시오.
# - 파일 정보 확인
# - 앞에서 3개의 행만 출력
# - 요약 통계량 보기
# - 흡연자, 비흡연자 수를 계산  : value_counts()
# - 요일을 가진 칼럼의 유일한 값 출력  : unique() -> 결과 : ['Sun' 'Sat' 'Thur' 'Fri']

df3 = pd.read_csv('../testdata/tips.csv')
print(df3)

# 파일 정보 확인
print("파일 정보 확인:")
print(df3.info())
print()

# 앞에서 3개의 행 출력
print("\n앞에서 3개의 행 출력:")
print(df3.head(3))
print()

# 요약 통계량 보기
print("\n요약 통계량 보기:")
print(df3.describe())
print()

# 흡연자, 비흡연자 수 계산
smoke_counts = df3['smoker'].value_counts()
print("\n흡연자, 비흡연자 수:")
print(smoke_counts)
print()

# 요일 칼럼의 유일한 값 출력
uni_days = df3['day'].unique()
print("\n요일 칼럼의 유일한 값:")
print(uni_days)