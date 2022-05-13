from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)

    class Meta:
        db_table='Category'
        verbose_name='category'
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name