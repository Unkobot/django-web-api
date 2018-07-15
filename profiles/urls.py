from django.urls import path
from .views import ProfileDetailView, ProfileListView

urlpatterns = [
    path('list/', ProfileListView.as_view(), name='list'),
    path('<str:username>/', ProfileDetailView.as_view(), name='detail'),
]