from django.shortcuts import render
from .models import Experience
# Create your views here.
def experience(request):
    experiences = Experience.objects.all()
    return render(request,'experience.html',{"experiences":experiences})