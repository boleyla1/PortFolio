from django.contrib import admin
from .models import *


class wblogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')


admin.site.register(Blog)
# Register your models here.
