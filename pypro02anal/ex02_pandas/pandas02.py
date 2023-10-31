# Reindexing, boolean processing, indexing support functions
import numpy as np
from pandas import Series, DataFrame

# Reindexing of Series
data = Series([1, 3, 2], index=(1, 4, 2))
print(data)

data2 = data.reindex((1, 2, 4))
print(data2)

print('Filling values when rearranging')
data3 = data2.reindex([0, 1, 2, 3, 4, 5])
# Empty values are treated as NaN
print(data3)

# Fill NaN with an arbitrary value
data3 = data2.reindex([0, 1, 2, 3, 4, 5], fill_value='Not seen')
print(data3)
print()

# Fill NaN with the previous row value
data4 = data2.reindex([0, 1, 2, 3, 4, 5], method='ffill')  # Forward Fill
print(data4)
print()

data4 = data2.reindex([0, 1, 2, 3, 4, 5], method='pad')  # Same as above
print(data4)
print()

# Fill NaN with the next row value
data4 = data2.reindex([0, 1, 2, 3, 4, 5], method='bfill')  # Back Fill
print(data4)
print()

data4 = data2.reindex([0, 1, 2, 3, 4, 5], method='backfill')  # Same as above
print(data4)
print()

print('Boolean processing')
df = DataFrame(np.arange(12).reshape(4, 3), index=['January', 'February', 'March', 'April'], columns=['Gangnam', 'Gangbuk', 'Seodaemun'])
print(df)
print(df['Gangnam'])
print(df['Gangnam'] > 3)
print(df[df['Gangnam'] > 3])

print('Indexing support functions: loc() - label support, iloc() - numeric support')
print(df.loc['March', :])
print(df.loc['March'])
print(df.loc[:'February'])
print(df.loc[:'February', ['Seodaemun']])
print()

print(df.iloc[2])
print(df.iloc[2, :])
print(df.iloc[:3])
print(df.iloc[:3, 2])
print(df.iloc[:3, 1:3])  # Less than 3 rows and columns from 1 to less than 3

print('\n\n\nOperations')
s1 = Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = Series([4, 5, 6, 7], index=['a', 'b', 'c', 'd'])
print(s1 + s2)  # NaN operation 3 == NaN / NaN in case of index mismatch
print(s1.add(s2))  # Inherits Numpy function
print(s1.sub(s2))
print(s1.mul(s2))
print(s1.div(s2))

print('Series Operations')
df1 = DataFrame(np.arange(9).reshape(3, 3), columns=list('kbs'), index=['Seoul', 'Daejeon', 'Busan'])
df2 = DataFrame(np.arange(12).reshape(4, 3), columns=list('kbs'), index=['Seoul', 'Daejeon', 'Jeju', 'Suwon'])

print(df1)
print(df2)

print(df1 + df2)
print(df1.add(df2, fill_value=0))

print()
print(df1)
seri = df1.iloc[0]
print(seri)
print(df1 - seri)  # DataFrame - Series

# Descriptive statistics related functions (methods)

df = DataFrame([[1.4, np.nan], [7, -4.5], [np.NaN, np.NAN], [0.5, -1]], columns=['one', 'two'])

print(df)
print(df.isnull())
print(df.notnull())
print(df.dropna(how='any'))  # Same as above
print(df.dropna(how='all'))
print(df.dropna(subset=['one']))  # Remove rows with NaN in a specific column
print(df.dropna(axis='rows'))
print(df.dropna(axis='columns'))
print()
print(df.fillna(0))

print('--------')
# Descriptive statistics related functions (methods)
print(df)
print(df.sum())
print(df.sum(axis=0))  # Sum of columns, Same as above
print(df.sum(axis=1))  # Sum of rows, Same as above

print()

print(df.mean(axis=1))
print(df.mean(axis=1, skipna=True))  # Exclude NaN from the calculation
print(df.mean(axis=1, skipna=False))  # Include NaN in the calculation
print(df.mean(axis=0, skipna=False))  # Exclude NaN from the calculation
print(df.mean(axis=0, skipna=True))  # Include NaN in the calculation

print()
print(df.describe())  # Print summary statistics

print(df.info())  # Print structure information
