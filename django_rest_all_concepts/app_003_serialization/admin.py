from django.contrib import admin
from app_003_serialization.models import *
# Register your models here.
@admin.register(detail)
class detailAdmin(admin.ModelAdmin):
    list_display = ['name', 'info', 'phone']