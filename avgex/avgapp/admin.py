
from django.contrib import admin

from avgapp.models import SurveyData


# Register your models here.

# Register your models here.
class SurveyAdmin(admin.ModelAdmin):
	list_display= ('id', 'job','gender','game_time')


admin.site.register(SurveyData, SurveyAdmin)

