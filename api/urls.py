from django.urls import path
from api.views import *
urlpatterns = [
    path("users/", UsersListView.as_view()),
    path("items/", ItemsListView.as_view()),
]
