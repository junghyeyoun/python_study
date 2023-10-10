# 반복문 while

a = 1

while a<=5:
    print(a,end=' ')
    a += 1
    
print()

i = 1
while i <=3:
    j = 1
    while j <= 4:
        print('i='+str(i)+"/j="+str(j))
        j = j+1
    i += 1
print('1~100 사이의 정수 중 3의 배수의 합')
i = 1; hap=0
while i <= 100:
    if i%3 == 0:
        hap+= i
    i += 1
print('합은 ' +str(hap))

print()
colors = 'r', 'g', 'b'
print(colors[1])
a = 0
while a<len(colors):
    print(colors[a], end=' : ')
    a += 1
    
print('별 찍기')
i=1
while i <= 10:
    j=1
    disp=' '
    while j<=i:
        disp += '*'
        j += 1
    print(disp)
    i+=1
    
print('\n 문1: 1~100 사이의 정수 중 3의 배수이고 2의 배수가 아닌 수를 출력하고 그 합을 출력')
sum = 0
i = 1  

while i <= 100:
    if i % 3 == 0 and not i % 2 == 0: 
        print(i  ,end=" ")
        sum = sum + i
    i = i + 1  
print('\n합은 ',sum)
        

print('\n 문2: 2~5단의 구구단. 단이 다르면 다음행으로 출력')
dan = 2
while dan <= 5:
    su = 1  
    while su <= 9:
        print(dan,'*',su,'=',dan * su ,end="  ")
        su += 1
    dan += 1 
    print()
    
import time

# time.sleep(3)
# print('계속')

button = input('폭탄 스위치를 누르까요?(y/n)')
if button == 'Y' or button == 'y':
    # pass
    count = 5
    while 1<= count:
        print('%d초 남았군요'%count)
        time.sleep(1)
        count -= 1
    print('폭발!')
elif button=='N' or button=='n':
    print('작업취소')
else:
    print('y or n을 누르시오')

    