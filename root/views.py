from django.shortcuts import render
from .models import Service , Skill , Team , Portfolio

# Create your views here.
def home (request):
    context = {
        'service' : Service.objects.filter(status = True),
        'skill' : Skill.objects.filter(status = True),
        'portfolio' : Portfolio.objects.filter(status = True),
        'team' : Team.objects.filter(status = True), 
    }
    return render(request , 'root/index.html' , context= context )