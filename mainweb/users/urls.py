from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import ProfileView

app_name = 'users'

urlpatterns = [
	# 계정 (... 생략 ...)

    # 프로필
    # user_id는 DB상의 인덱스
    # path('profile/base/<int:user_id>/', ProfileView.profile_base, name='profile_base'),
    path('profile/<int:user_id>/', ProfileView.ProfileCommentListView.as_view(), name='profile'),
]