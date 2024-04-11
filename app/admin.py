from django.contrib import admin
from .models import Task 
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = "title","task"
    list_editable = "task"
    list_per_page = 1
    list_filter = "task"

admin.site.register(Task)