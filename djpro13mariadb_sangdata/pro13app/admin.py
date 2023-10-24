from django.contrib import admin
import djpro13mariadb_sangdata
from pro13app.models import Sangdata

# Register your models here.
class SangAdmin(admin.ModelAdmin):
    list_dispaly=('code','sang','su','dan')
admin.site.register(Sangdata, SangAdmin)