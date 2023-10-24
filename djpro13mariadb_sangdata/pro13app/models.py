from django.db import models

# Create your models here.
class Sangdata(models.Model):
    code = models.IntegerField(primary_key=True)
    sang = models.CharField(max_length=20, blank=True, null=True)
    su = models.IntegerField(blank=True, null=True)
    dan = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sangdata'
        
"""
1. 기본 값(True): managed 속성이 기본적으로 True로 설정되어 있으며, 이 경우 Django는 이 모델을 데이터베이스와 관리합니다. 
즉, 모델 클래스를 사용하여 데이터베이스 스키마를 생성, 수정 및 관리합니다. 
모델 클래스의 변경 사항(새 모델 추가, 필드 수정 등)을 makemigrations 및 migrate 명령을 사용하여 데이터베이스에 적용할 수 있습니다.

2. False: managed 속성을 False로 설정하면 Django는 해당 모델을 데이터베이스와 관리하지 않습니다. 
이 모델은 외부 데이터베이스와 연결되거나 데이터베이스 스키마가 외부 소스에서 관리되는 경우에 유용합니다. 
이 모델을 사용하여 데이터를 읽을 수 있지만 데이터베이스에 쓰는 작업은 수행하지 않습니다.
"""