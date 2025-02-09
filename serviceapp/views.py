from django.shortcuts import render
from mainapp.models import *
from .models import *


def service(request):
    faq = Faq.objects.all()
    projects = Project.objects.all()
    return render(request, 'serviceapp/services.html', {'projects':projects , 'faq':faq})
# Create your views here.
