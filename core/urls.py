from django.urls import path
from . import views
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('api/v1/about', views.apiabout, name='api')
]