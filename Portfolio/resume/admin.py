from django.contrib import admin
from .models import Resume
# Register your models here.

class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id','created_at']

admin.site.register(Resume,ResumeAdmin)