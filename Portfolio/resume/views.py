from django.shortcuts import render
from .models import Resume
# Create your views here.
def resume(request):
    resume = Resume.objects.all()
    return render(request,'resume.html',{"resume":resume})