from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
     list_display = ('id','name','address','city','state','pincode')
admin.site.register(Student,StudentAdmin)