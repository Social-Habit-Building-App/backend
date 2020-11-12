from django.shortcuts import render
from accounts.models import userProfile

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .serializers import UserSerializer, HabitSerializer

from tracker.models import Habit, Progress  

class UsersListView(generics.ListAPIView):
    queryset = userProfile.objects.all()
    serializer_class = UserSerializer

class HabitListView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

@api_view(['GET', 'POST'])
def userHabits(request, pk):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        user = userProfile.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'POST':
        user = userProfile.objects.get(pk=pk)
        habit = Habit(habit_name=request.data['habit_name'], user=user)
        habit.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def habitProgress(request, pk, habit_name):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        user = userProfile.objects.get(pk=pk)
        habit = user.habits.get_queryset().get(habit_name=habit_name)
        serializer = HabitSerializer(habit)
        return Response(serializer.data)

    elif request.method == 'POST':
        user = userProfile.objects.get(pk=pk)
        habit = user.habits.get_queryset().get(habit_name=habit_name)
        progress = Progress(units_value=request.data['units_value'], habit=habit)
        progress.save()
        return Response(progress.pub_date, status=status.HTTP_201_CREATED)