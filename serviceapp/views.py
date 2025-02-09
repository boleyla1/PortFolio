from django.shortcuts import render
from mainapp.models import *


def service(request):
    projects = Project.objects.all()
    return render(request, 'serviceapp/services.html', {'projects':projects})
# Create your views here.
