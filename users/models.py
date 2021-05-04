from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User

class Leave(models.Model):
    title = models.CharField(max_length=32,unique=True)
    description = models.TextField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title

class GetLeave(models.Model):
    leave = models.ForeignKey(Leave, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    days = models.FloatField(default=0)