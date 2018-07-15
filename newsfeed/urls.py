from django.urls import path
from .views import NewsfeedApiCreate, NewsfeedApiDelete, NewsfeedApiUpdate, NewsfeedApiView, NewsfeedDeleteView, NewsfeedDetailView, NewsfeedCreateView, NewsfeedUpdateView

urlpatterns = [
    path('<int:pk>/<slug:slug>/', NewsfeedDetailView.as_view(), name="newsfeed"),
    path('create/', NewsfeedCreateView.as_view(), name="create"),
    path('update/<int:pk>/', NewsfeedUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', NewsfeedDeleteView.as_view(), name="delete"),
    path('api/v1/view/', NewsfeedApiView.as_view(), name="newsapiview"),
    path('api/v1/create/', NewsfeedApiCreate.as_view(), name="newsapicreate"),
    path('api/v1/update/<int:pk>/', NewsfeedApiUpdate.as_view(), name="newsapiupdate"),
    path('api/v1/delete/<int:pk>',NewsfeedApiDelete.as_view(), name="newsapidelete"),
]