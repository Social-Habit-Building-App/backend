from django.urls import path, include

from .views import UsersListView, UserDetailView, HabitListView


urlpatterns = [
    path('users/all', UsersListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('habits/all', HabitListView.as_view()),
]
