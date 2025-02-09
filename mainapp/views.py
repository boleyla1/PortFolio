from django.shortcuts import render
from .models import Skill, Project , RecentProject,Service



def index(request):
    Projects = Project.objects.all()
    Skills = Skill.objects.all()
    RecentProjects = RecentProject.objects.all()
    Services = Service.objects.all()
    return render(request, 'mainapp/index.html', {"projects": Projects, 'skills': Skills,
                                                  'recent_projects': RecentProjects, 'services': Services})


def about(request):
    return render(request, 'about/about.html')
