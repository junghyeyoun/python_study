from django.db import models

# Create your models here.
class Maker(models.Model):
    mname = models.CharField(max_length=20)
    mtel = models.CharField(max_length=30)
    maddr = models.CharField(max_length=50)
    def __str__(self):
        return self.mname # 테이블이 두개 있을 때는 꼭 필요함. => id 대신 name으로 나오게 할 것이라는 뜻
    
class Product (models.Model):
    pname = models.CharField(max_length=20)
    pprice = models.IntegerField()
    pmaker_name = models.ForeignKey(Maker, on_delete=models.CASCADE)  # fk는 Maker의 pk(id)를 참조  
    # on_delete=models.CASCADE => Maker에 있는거 지우면 Maker 참조받는 Product 다 지우짐
    
    
    