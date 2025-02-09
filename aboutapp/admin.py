from django.contrib import admin

from .models import *


class CountAdmin(admin.ModelAdmin):
    list_display = ('years', 'projectCompeletes', 'Smiles')  # نمایش فیلدها در لیست ادمین
    # list_editable = ('years', 'projectCompeletes', 'Smiles')  # قابل ویرایش کردن فیلدها


admin.site.register(Count, CountAdmin)

admin.site.register(Comment)

# Register your models here.
