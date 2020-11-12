from django.urls import path, include

from .views import UsersListView, HabitListView, habitProgress, userHabits


urlpatterns = [
    path('users/all', UsersListView.as_view()),
    path('users/<slug:pk>/', userHabits),
    path('users/<slug:pk>/habits/<slug:habit_name>/', habitProgress),
    path('habits/all', HabitListView.as_view()),
]
