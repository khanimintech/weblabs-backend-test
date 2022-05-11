from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)

    class Meta:
        db_table='Category'
        verbose_name='category'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name
        
class Portfolio(models.Model):
    name=models.CharField(max_length=50)
    picture=models.ImageField(upload_to='portfolio_images')
    created_date=models.DateTimeField(auto_now_add=True)
    category=models.ManyToManyField(Category,related_name='portfolio')
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='portfolio',null=True)


    class Meta:
        db_table='Portfolio'
        verbose_name='portfolio'
        verbose_name_plural='Portfolio'

    def __str__(self):
        return self.name

