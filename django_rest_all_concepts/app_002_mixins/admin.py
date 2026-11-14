from django.contrib import admin
from app_002_mixins.models import *
# Register your models here.
@admin.register(testInfo)
class testInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'address']
    search_fields = ('name', 'phone')