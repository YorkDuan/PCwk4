from django.db import models
from django.contrib.auth.models import Author, User


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    pubdate = models.DateField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    subject = models.CharField(max_length=50)
    #author = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField(max_length=999)
    number_of_books = models.IntegerField(default=12)



