from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from users.views import ProfileView

app_name = 'users'

urlpatterns = [
	# 계정 (... 생략 ...)

    # 프로필
    # pk는 DB상의 인덱스
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/update/', views.profile_update, name='profile_update')  
]