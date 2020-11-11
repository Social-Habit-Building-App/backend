from django.contrib import admin
from .models import Habit

class HabitAdmin(admin.ModelAdmin):
    fields = ['habit_name']

admin.site.register(Habit, HabitAdmin)