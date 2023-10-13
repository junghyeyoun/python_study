# https://cafe.daum.net/flowlife/RUrO/24 => 문제 4번

from abc import ABCMeta, abstractmethod

class Employee(metaclass = ABCMeta):
    
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai
    
    @abstractmethod
    def pay(self, pay):
        pass
        
    @abstractmethod
    def data_print(self):
        print('이름 : '+self.irum+', 나이 : ',format(self.nai), end=' ')
    
    def irumnai_print(self):
        pass