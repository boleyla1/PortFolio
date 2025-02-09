# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('wblog/', views.blog_list, name='blogs'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
]
