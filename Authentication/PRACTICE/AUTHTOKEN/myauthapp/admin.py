from django.contrib import admin

# Register your models here.
from .models import Student

@admin.register(Student)
class StudentModel(admin.ModelAdmin):
    list_display=["id","name",'roll']