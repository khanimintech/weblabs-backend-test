from django.db import models
from .category import Category
from django.contrib.auth.models import User


class Portfolio(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    picture=models.ImageField(upload_to='portfolio_images')
    created_date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='portfolio',null=True)
    status=models.BooleanField(default=True)


    class Meta:
        db_table='Portfolio'
        verbose_name='portfolio'
        verbose_name_plural='Portfolio'

    def __str__(self):
        return self.name