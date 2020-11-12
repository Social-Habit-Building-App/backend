from rest_framework import serializers
from django.contrib.auth.models import User
from tracker.models import Habit, Progress

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['units_value', 'pub_date']

class HabitSerializer(serializers.ModelSerializer):
    progresses = ProgressSerializer(many=True)
    class Meta:
        model = Habit
        fields = ['habit_name', 'progresses']

class UserSerializer(serializers.ModelSerializer):
    habits = HabitSerializer(many=True)
    class Meta:
        model = User
        fields = ['username', 'habits']