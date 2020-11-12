from django.urls import path, include

from .views import UsersListView, HabitListView, habitProgress, userHabits


urlpatterns = [
    path('users/all', UsersListView.as_view()),
    path('users/<slug:username>/', userHabits),
    path('users/<slug:username>/habits/<slug:habit_name>/', habitProgress),
    path('habits/all', HabitListView.as_view()),
]
