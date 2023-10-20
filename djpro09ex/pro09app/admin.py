from django.contrib import admin
from pro09app.models import Friend

# Register your models here.
class FriendAdmin(admin.ModelAdmin):
    list_display = ('irum','juso','nai') # 보고 싶은 내용 보기
    
admin.site.register(Friend, FriendAdmin)