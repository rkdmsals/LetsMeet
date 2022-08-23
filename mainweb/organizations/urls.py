from django.urls import path, include
from .views import MoimListView, MoimDetailView

urlpatterns = [
    path('list/', MoimListView.as_view(), name='moim-list'),
    path('detail/<uuid:pk>', MoimDetailView.as_view(), name='moim-detail-view'),
]