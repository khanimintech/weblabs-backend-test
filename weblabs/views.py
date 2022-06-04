import re
from sre_constants import CATEGORY
from django.shortcuts import render
from .models import Portfolio, Contact
from weblabs.models import Contact,Category
from django.core.paginator import Paginator
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect

def home(request):
    projects=Portfolio.objects.order_by('-id')
    last_projects=projects[0:6]
    context={
        'projects':projects,
        'last_projects':last_projects
    }
    return render (request, 'index.html',context)

def about(request):
    projects=Portfolio.objects.all()
    completed_projects_count=Portfolio.objects.filter(status=True).count()
    not_completed_projects_count=Portfolio.objects.filter(status=False).count()

    context={
        'completed_projects_count':completed_projects_count,
        'not_completed_projects_count':not_completed_projects_count
    }
   
    return render (request, 'about.html', context)

def services(request):

    return render (request, 'services.html')

def site_services(request):
    
    return render (request, 'site_services.html')

def technical_services(request):
    
    return render (request, 'technical_services.html')

def seo_services(request):
        
    return render (request, 'seo_services.html')

def design_services(request):
        
    return render (request, 'design_services.html')

def smm_services(request):
        
    return render (request, 'smm_services.html')

def all_projects(request):
    search=request.GET.get('search')
    number=request.GET.get('page')
    projects=Portfolio.objects.order_by('-created_date')
    categories=Category.objects.all()
    if search:
        projects=projects.filter(name__icontains=search)
    projects=Paginator(projects, 4)
    context={
        'projects':projects.get_page(number),
        'categories':categories
    }
    return render(request, 'projects.html',context)

def category_detail(request, category_slug):
    projects=Portfolio.objects.all().filter(category__slug=category_slug)
    categories=Category.objects.all()

    context={
        'projects':projects,
        'categories':categories
    }
    
    return render(request, 'projects.html', context)
    

def contact(request):
    form=ContactForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            form.save()
            name=form.cleaned_data.get('name')
            surname=form.cleaned_data.get('surname')
            email=form.cleaned_data.get('email')
            message=f"Hormetli {name} {surname} mesajınız çatdı. Sizinlə tezliklə əlaqə saxlanılacaq. Təşəkkürlər!"
            send_mail(
                subject='weblabs',
                message=message,
                from_email=None,
                recipient_list=[email],
                fail_silently=False
            )

            return redirect('contact')

    return render(request,'contact.html',{'form':form})