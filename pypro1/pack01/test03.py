# tuple : list와 유사하나 읽기 전용(list보다 처리 속도가 빠름)

t = 'a','b','c' # = t = ('a','b','c')
print(t,type(t),len(t))
print(type(tuple()))

# p = (1) -> 1 <class 'int'>
p = (1,) # ,를 줘야 튜플로 인정
print(p, type(p))
print(t[0])
# t[0]= 'k' # 'tuple' object does not support item assignment
li = list(t) # 형변환
li[0] = 'k'
t = tuple(li)
print(t, type(t))

# p = (1) # l <class'int>
p = (1,)
print(p, type(p))

print('set------------------------------------')
# set type : 순서x, 수정x. 중복 불가
a = {1,2,3}
print(a,type(a))
print(type(set()))
# print(a[0]) -> TypeError: 'set' object is not subscriptable (인덱싱불가)
# a[0] = 10 -> 인덱싱이 안되기 때문에 수정또한 불가

b = {3,4}
print(a.union(b)) # 합집합
print(a.intersection(b)) # 교집합
print(a -b,a|b,a&b) #차, 합, 교집합

print()
b.update({6,7}) # 원소 추가
print(b)

b.discard(7) # 값에 의한 삭제
# b.remove(8) # 값에 의한 삭제
b.discard(7) # 값에 의한 삭제 - 해당 값이 없으면 통과
# b.remove(8) # 값에 의한 삭제 - 해당 값이 있으면 에러
print(b)

li = ['tom', 'oscar', 'tom']
s = set(li)
li = list(s)
print(li)

print('dict-------------------------------------')
# dict type : 키:값의 형태로 쌍을 이룸. 순서x, 키를 이용해 값을 조회
mydic =dict(k1=1,k2='123',k3=3.4)
print(mydic,type(mydic)) # {'k1': 1, 'k2': '123', 'k3': 3.4} <class 'dict'>

dic={'파이썬':'뱀','자바':'커피','스프링':'봄', '숫자':[1,2,3]}
print(mydic,type(mydic),len(dic))
print(dic['자바']) # 키로 값을 참조
# print(dic['커피']) # KeyError :'커피'
dic['자바'] ='프로그래밍언어' # 해당 키로 값을 수정
print(dic)
dic['오라클'] = '예언자' # 추가
print(dic)
del dic['오라클'] # 삭제
dic.pop('숫자') # 삭제
print(dic)
print(dic.keys())
print(dic.values())