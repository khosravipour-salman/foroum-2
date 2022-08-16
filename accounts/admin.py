from django.contrib import admin
from .models import UserModel

class CustomUser(admin.ModelAdmin):
	search_fields = ['age','gender']
	list_display= ('age','gender','user','phone_number')

admin.site.register(UserModel,CustomUser)
