from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from users.views import ProfileView

app_name = 'users'

urlpatterns = [
	# 계정 (... 생략 ...)

    # 프로필
    # user_pk는 DB상의 인덱스
    path('profile/<int:user_pk>/', ProfileView.as_view(), name='profile'),
    path('profile/', views.profile_update, name='profile_update')  
]