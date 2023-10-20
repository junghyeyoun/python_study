from django.contrib import admin
from pro08app.models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','code','name','price','pub_date') # 보고 싶은 내용 보기
    
admin.site.register(Article, ArticleAdmin)