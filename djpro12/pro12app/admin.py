from django.contrib import admin
from pro12app.models import Maker, Product

# Register your models here.
class MakerAdmin(admin.ModelAdmin):
    list_display = ('id','mname','mtel','maddr')
admin.site.register(Maker, MakerAdmin)
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','pname','pprice','pmaker_name')
admin.site.register(Product, ProductAdmin)