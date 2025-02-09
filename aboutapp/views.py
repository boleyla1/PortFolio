from django.shortcuts import render
from .models import Count


def about(request):
    come = Count.objects.first()  # دریافت همه اشیاء
    return render(request, 'about/about.html', {'come': come})
