from django.urls import path
from . import views

urlpatterns = [
    path('vice/', views.service, name='service'),
]