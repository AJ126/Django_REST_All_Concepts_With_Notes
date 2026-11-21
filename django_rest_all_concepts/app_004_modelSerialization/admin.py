from django.contrib import admin
from app_004_modelSerialization.models import *
# Register your models here.
@admin.register(information)
class informationAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']