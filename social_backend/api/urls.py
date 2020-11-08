from django.urls import path, include

from .views import UsersListView, UserDetailView, HabitListView, habitProgress


urlpatterns = [
    path('users/all', UsersListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('users/<int:pk>/habits/<slug:habit_name>/', habitProgress),
    path('habits/all', HabitListView.as_view()),
]
