from django.urls import path, include
from allauth.account import views as aview
from . import views

urlpatterns = [
    path('', views.sociallogin, name='sociallogin'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', aview.SignupView.as_view(), name='register'),

    # https://medium.com/chanjongs-programming-diary/django-rest-framework%EB%A1%9C-%EC%86%8C%EC%85%9C-%EB%A1%9C%EA%B7%B8%EC%9D%B8-api-%EA%B5%AC%ED%98%84%ED%95%B4%EB%B3%B4%EA%B8%B0-google-kakao-github-2ccc4d49a781
    # path('google/login', views.google_login, name='google_login'),
    # path('google/callback/', views.google_callback, name='google_callback'),  
    # path('google/login/finish/', views.GoogleLogin.as_view(), name='google_login_todjango'),
]