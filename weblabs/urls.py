from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('about', views.about,name="about"),
    path('allprojects', views.all_projects,name="all_projects")
] 