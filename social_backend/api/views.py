from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .serializers import UserSerializer, HabitSerializer

from tracker.models import Habit, Progress  

class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class HabitListView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

@api_view(['GET', 'POST'])
def userHabits(request, username):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'POST':
        user = User.objects.get(username=username)
        habit = Habit(habit_name=request.data['habit_name'], user=user)
        habit.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def habitProgress(request, username, habit_name):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        user = User.objects.get(username=username)
        habit = user.habits.get_queryset().get(habit_name=habit_name)
        serializer = HabitSerializer(habit)
        return Response(serializer.data)

    elif request.method == 'POST':
        user = User.objects.get(username=username)
        habit = user.habits.get_queryset().get(habit_name=habit_name)
        progress = Progress(units_value=request.data['units_value'], habit=habit)
        progress.save()
        return Response(progress.pub_date, status=status.HTTP_201_CREATED)