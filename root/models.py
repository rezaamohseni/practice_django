from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title
class Team(models.Model):
    image = models.ImageField(upload_to= 'root' , default='default.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ManyToManyField(Skill)
    description = models.TextField()
    status = models.BooleanField(default=False)  
    
    def __str__(self):
        return self.user.username
class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)


    def __str__(self):
        return self.title
    
class Portfolio(models.Model):
    image = models.ImageField(upload_to= 'portfolio' , default='default.jpg')
    status = models.BooleanField(default=True)


    
# Create your models here.
