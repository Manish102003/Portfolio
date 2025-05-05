from django.contrib import admin
from .models import Project
# Register your models here.


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Project,ProjectsAdmin)