from django.urls import path, include

from .views import *


urlpatterns = [
    path('users/all', UsersListView.as_view()),
]
