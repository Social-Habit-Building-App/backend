from rest_framework import serializers
from django.contrib.auth.models import User
from tracker.models import Habit


class UserSerializer(serializers.ModelSerializer):
    habits = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = ['username', 'habits']