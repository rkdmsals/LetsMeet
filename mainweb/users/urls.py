from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # pk는 DB상의 인덱스

    # path('profile/<int:pk>/', profile_view.as_view(), name='profile'),
    # path('profile/<int:pk>/update/', views.profile_update_view, name='profile_update')  
    
    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.profile_update_view, name='profile_update'),
]