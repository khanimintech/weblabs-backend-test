from django.db import models
from ckeditor.fields import RichTextField


class Contact(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    message=RichTextField()

    class Meta:
        db_table='Contact'
        verbose_name='message'
        verbose_name_plural='Messages'

    def __str__(self):
        return self.email