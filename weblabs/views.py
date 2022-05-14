from django.shortcuts import render
from .models import Portfolio
from django.core.paginator import Paginator

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

def all_projects(request):
    search=request.GET.get('search')
    number=request.GET.get('page')
    projects=Portfolio.objects.order_by('-created_date')
    if search:
        projects=projects.filter(name__icontains=search)
    projects=Paginator(projects, 4)
    context={
        'projects':projects.get_page(number)
    }
    return render(request, 'projects.html',context)

