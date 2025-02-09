from django.shortcuts import render
from .models import Count, Comment
from mainapp.models import Project
from weblog.models import Blog


def about(request):
    come = Count.objects.first()  # دریافت همه اشیاء\
    comment = Comment.objects.all()
    Projects = Project.objects.all()
    Blogs = Blog.objects.all()
    return render(request, 'about/about.html', {'come': come, comment: comment, "Projects": Projects, "Blogs": Blogs})
