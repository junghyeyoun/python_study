# pandas로 파일 읽기
import pandas as pd 
# df = pd.read_csv('../testdata/ex1.csv')
df = pd.read_csv('https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/ex1.csv') # 웹에서 읽어오기
print(df, type(df))
print()
df = pd.read_table('../testdata/ex1.csv',sep=',')
print(df)
print()
df = pd.read_csv('../testdata/ex2.csv',header=None)
print(df)
df = pd.read_csv('../testdata/ex2.csv',header=None,names=['col1','col2'])
print(df)
print()
df = pd.read_csv('../testdata/ex2.csv',header=None,names=['col1','col2'])
print(df)
df = pd.read_csv('../testdata/ex2.csv',header=None,names=['a','b','c','d','msg'],index_col='msg')
print(df)
print()
# df = pd.read_csv('../testdata/ex3.txt')
df = pd.read_csv('../testdata/ex3.txt',sep='\s ') # sep=' ' / sep='정규표현식'
# 정규 표현식
# \s : space를 표현하며 공백 문자를 의미
# \S : non space를 표현하며 공백 문자가 아닌 것을 의미한다.
print(df)
print(df.info())
print(df.describe())
print()
df = pd.read_table('../testdata/ex3.txt',sep='\s+',skiprows=(1,3)) # 특정 행 제거
print(df)

print()
df = pd.read_fwf('../testdata/data_fwt.txt',widths=(10,3,5),header=None,names=('date','name','price'))
print(df)

print()
# 대용량의 자료를 chunk(묶음) 단위로 할당해서 처리 가능
test = pd.read_csv('../testdata/data_csv2.csv',header=None,chunksize=3)
print(test) # TextFileReader object (텍스트 파서 객체)

for p in test:
    # print(p)
    print(p.sort_values(by=2,ascending=True))
    
print('\n\nDataFrame 저장')
items = {'apple':{'count':10,'price':1500}, 'orange':{'count':5,'price':1000}}
df = pd.DataFrame(items)
print(df)
# print(df.to_html())
# print(df.to_json())
# print(df.to_clipboard()) # 붙여넣기
# print(df.to_csv())
df.to_csv('test01.csv',sep=',')
df.to_csv('test02.csv',sep=',',index=False)
df.to_csv('test03.csv',sep=',',index=False,header=False)