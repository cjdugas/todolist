from django.contrib import admin
from core.models import List, Task


class TaskInLine(admin.TabularInline):
    model = Task
    extra = 1


class ListAdmin(admin.ModelAdmin):
    #list_display = ('title', 'description')
    inlines = [TaskInLine]
    search_fields = ['title']


admin.site.register(List, ListAdmin)
