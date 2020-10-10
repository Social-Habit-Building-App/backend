from django.db import models

# from _ import User


class Habit(models.Model):
    habit_name = models.CharField(max_length=100)
    
    # uncomment this line if you added User model 
    # users = models.ManyToManyField(User)
    
    def __str__(self):
        return self.habit_name