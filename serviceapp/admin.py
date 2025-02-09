from django.contrib import admin
from .models import Faq


class FaqAdmin(admin.ModelAdmin):
    list_display = ('Faq', 'Question', 'Answer')


admin.site.register(Faq)
# Register your models here.
