from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    image = models.ImageField()
    user = models.ForeignKey()
    
# Create your models here.
