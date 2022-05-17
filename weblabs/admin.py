from django.contrib import admin
from .models import Category,Portfolio,Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

class PortfolioAdmin(admin.ModelAdmin):
    list_display=['name','created_date','author']
    list_display_links=['name','created_date']
    search_fields=['name']
    list_filter=['name']


admin.site.register(Portfolio,PortfolioAdmin)
admin.site.register(Contact)

