import numpy as np
import pandas as pd
from pandas import DataFrame, Series

# Series: 1-dimensional array-like structure with an index for indexing the data.
# 1-dimensional array of indexed data
obj = pd.Series([3, 7, -5, 5])
# obj = pd.Series((3, 7, -5, 5))                # Sets are not allowed, as they are unordered and indexing is not possible
# obj = pd.Series({3, 7, -5, 5})                # Automatic indexing
print(obj)

# Creating a Series with custom index
obj2 = pd.Series([3, 7, -5, 5], index=['a', 'b', 'c', 'd'])
print(obj2, type(obj2))
print(obj2.sum(), sum(obj2), np.sum(obj2))
print(obj2.values)
print(obj2.index)

# Indexing / Slicing
print(obj2['a'])
print(obj2[['a']])
print(obj2[['a', 'b']])
print(obj2['a':'c'])

print(obj2[2])
print(obj2[1:4])
print(obj2[[2, 1]])
print(obj2 > 0)
print('a' in obj2)

# Dictionary type: Processing with Series objects
names = {'mouse': 5000, 'keyboard': 25000, "monitor": 550000}
print(names)
obj3 = Series(names)
print(obj3, type(obj3))
obj3.index = ['마우스', '키보드', '모니터']
print(obj3)
print(obj3[0], ' ', obj3['마우스'])

obj3.name = '상품가격'
print(obj3)

# DataFrame: Tabular structure - A shape of multiple Series
df = DataFrame(obj3)
print(df)

data = {
    'irum': ['한국인', '중국인', '일본인', '러시아인'],
    'juso': ('사당', '베이징', '도쿄', '모스크바'),
    'nai': [26, 25, 32, 27],
}
print(data, type(data))

df2 = pd.DataFrame(data)
print(df2, type(df2))
print(df2['irum'], type(df2['irum']))
print(df2.irum, type(df2.irum))
# Each column of DataFrame is a Series type
print()

print(DataFrame(data, columns=['juso', 'irum', 'nai']))
print(df2)

print('Filling NaN for values not in data')
df3 = pd.DataFrame(data)
print(DataFrame(data, columns=['irum', 'juso', 'nai', 'tel'],
                index=['a', 'b', 'c', 'd']))
print(df3)

# Adding values to the 'tel' column
df3['tel'] = '111-1111'
print(df3)

# Adding values to the 'tel' column using a Series
tvalue = Series(['222-2222', '333-3333', '444-4444'], index=['b', 'c', 'd'])
df3['tel'] = tvalue
print(df3)

print()

# Transpose
print('Transpose')
print(df3.T)

print(df3.values)
# ndarray type: No (,) in shape
print(df3.values[0, 1])  # indexing
print(df3.values[0:2])  # slicing

# Deleting rows or columns
print('Deleting rows or columns')
df4 = df3.drop([3], axis=0)  # Drop Row
df4 = df4.drop('tel', axis=1)  # Drop Column
print(df4)

# Sorting
print('Sorting')
print(df4.sort_index(axis=0, ascending=False))  # Row-wise
print()
print(df4.sort_index(axis=0, ascending=True))  # Column-wise Ascending: irum juso nai / Descending: nai juso irum
print()
print(df4.rank(axis=0))  # Rank in lexicographic order

print()
counts = df4['juso'].value_counts()
print('Number of values in column: ', counts)

# String splitting
print('String splitting')
data = {
    'juso': ['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon': [23, 25, 21],
}
fr = DataFrame(data)
print(fr)

# Splitting the 'juso' column into two separate columns
result1 = Series([x.split()[0] for x in fr.juso])
print(result1)
result2 = Series((x.split()[1] for x in fr.juso))
print(result2)
