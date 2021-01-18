from django.contrib import admin
from .models import *
# Register your models here.

class CourAdmin(admin.ModelAdmin):
    list_display = ('title','imgUrl','ytUrl','description','done')

admin.site.register(Course,CourAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','done','date','created_at')

admin.site.register(Item,TaskAdmin)