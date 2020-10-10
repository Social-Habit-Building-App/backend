from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics

from .serializers import *


class UsersListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
