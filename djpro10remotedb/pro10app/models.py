from django.db import models

# Create your models here.
class Guest(models.Model):
    # myno = models.AutoField(auto_created = True, primary_key = True)
    title = models.CharField(max_length=100)
    content=models.TextField()
    regdate=models.DateTimeField()
    
    def __str__(self):  # 얘를 썻기 때문에 views의 11번째에 id 값을 찍지 않고 제목인 '연습'을 출력하게 됨
        return self.title
    
    class Meta:
        # 정렬 방법 1 : 
        # ordering = ('title',) # tuple 타입으로 기술 => , 써야함
        # ordering = ('title','-id')
        ordering = ('-id',)