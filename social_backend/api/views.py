from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework import generics

from .serializers import UserSerializer

from tracker.models import Habit    
from tracker.serializers import HabitSerializer

class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HabitListView(generics.ListAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer