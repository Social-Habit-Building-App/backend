from django.db import models
from accounts.models import userProfile


class Habbit(models.Model):
    user = models.ForeignKey(userProfile, on_delete=models.CASCADE)
    habbit_name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.habbit_name
