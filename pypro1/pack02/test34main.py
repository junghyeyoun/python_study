# https://cafe.daum.net/flowlife/RUrO/24 => 문제 4번

from pack02.test34etc import Employee

class Temporary(Employee):
    def __init__(self, irum, nai ,ilsu, ildang):
        Employee.__init__(self, irum, nai)
        self.ilsu = ilsu
        self.ildang = ildang
        
    def pay(self):
        self.pay = self.ilsu*self.ildang 
    
    def data_print(self):
        super().data_print()  
        print(',월급: ',format(self.pay))

t = Temporary('홍길동',23,20,15000)
t.pay()
t.data_print()

class Regular(Employee):
    def __init__(self, irum, nai, salary):
        Employee.__init__(self, irum, nai)
        self.salary = salary
        
    def pay(self):
        pass
    
    def data_print(self):
        super().data_print() 
        print(', 급여 : ',format(self.salary), end=' ')
    
r = Regular('한국인',27,3500000)
r.data_print()
    
class Salesman(Regular):
    def __init__(self,irum, nai, salary,sales, commision):
        Regular.__init__(self, irum, nai, salary)
        self.sales = sales
        self.commision = commision
        
    def pay(self):
        self.pay = self.salary + (self.sales * self.commision)
        
    def data_print(self):
        print()
        super().data_print()
        print(',수령액 : ',format(self.pay))
        
s = Salesman('손오공',29,1200000,5000000,0.25)
s.pay()
s.data_print()
        