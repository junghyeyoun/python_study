from django.contrib import admin
from pro11app.models import Family

# Register your models here.
class FamilyAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','tel','gen')
    
admin.site.register(Family)