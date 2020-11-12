from django.db import models
from accounts.models import userProfile


class Habit(models.Model):
    habit_name = models.CharField(max_length=100)
    user = models.ForeignKey(userProfile, related_name = 'habits', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.habit_name


class Progress(models.Model):
    pub_date = models.DateField(auto_now_add=True)
    units_value = models.IntegerField()
    habit = models.ForeignKey(Habit, related_name = 'progresses', on_delete=models.CASCADE)