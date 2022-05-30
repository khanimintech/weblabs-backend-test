from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('saytların-hazırlanması', views.site_services, name="site_services"),
    path('texniki-dəstək', views.technical_services, name="technical_services"),
    path('seo-xidməti', views.seo_services, name="seo_services"),
    path('dizayn-xidməti', views.design_services, name="design_services"),
    path('smm-xidməti', views.smm_services, name="smm_services"),
    path('allprojects', views.all_projects, name="all_projects"),
    path('contact',views.contact,name='contact'),
    path('categories/<slug:category_slug>',views.category_detail,name='projects_by_category'),
] 