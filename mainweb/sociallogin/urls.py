from django.urls import path, include
from . import views

urlpatterns = [
    #path('sociallogin/', include('allauth.urls')),
    path('', views.sociallogin, name='sociallogin'),
    path('logout/', views.logout_view, name='logout'),
]