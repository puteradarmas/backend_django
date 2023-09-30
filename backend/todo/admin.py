from django.contrib import admin

# Register your models here.
from .models import todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','description','completed')
    
admin.site.register(todo,TodoAdmin)


