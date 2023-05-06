from django.contrib import admin
from .models import Student,Teacher
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=["id","name","roll","dept","image"]

    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=["id","name",'roll',"dept"]