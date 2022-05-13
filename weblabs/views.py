from django.shortcuts import render
from .models import Portfolio

def home(request):
    projects=Portfolio.objects.order_by('-id')
    last_projects=projects[0:6]

    context={
        'projects':projects,
        'last_projects':last_projects
    }
    return render (request, 'index.html',context)

def about(request):
    return render (request, 'about.html')
