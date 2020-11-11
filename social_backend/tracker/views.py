from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Habit

def habitview(request):
    model = Habit
    output = '\n'.join([h.habit_name for h in model.objects.all()])
    return HttpResponse(output)