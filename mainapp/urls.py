from django.urls import path
from . import views
from portfolio import settings
import static

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about')
]
