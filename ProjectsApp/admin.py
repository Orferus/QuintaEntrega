from django.contrib import admin
from ProjectsApp.models import Task, Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'begin', 'end', 'active')
    search_fields = ('name','active')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'begin', 'end','project','active')
    search_fields = ('name', 'active') 
    list_filter = ('name', 'project',)

admin.site.register(Task,TaskAdmin)
admin.site.register(Project, ProjectAdmin)