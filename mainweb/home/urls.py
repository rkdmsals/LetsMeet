from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('design/', views.design, name='design'),
]