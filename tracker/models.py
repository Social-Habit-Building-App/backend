from django.db import models
from accounts.models import userProfile
#from django.contrib.auth.models import User


class Habit(models.Model):
    habit_name = models.CharField(max_length=100)

    user = models.ForeignKey(
        userProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.habit_name
