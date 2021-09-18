from django.core import validators
from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Author(models.Model):
    first_name= models.CharField(max_length=10)
    last_name=models.CharField(max_length=20)
    email= models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption =models.CharField(max_length=50)
    
    def __str__(self):
        return self.caption


class Post(models.Model):
    title=models.CharField(max_length=20)
    img_name=models.CharField(max_length=50)
    date=models.DateField(auto_now=True)
    slug= models.SlugField(unique=True,db_index=True)
    author= models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,related_name="posts")
    # content=models.TextField(validators=
    #         [MinLengthValidator(10)] )
    tag=models.ManyToManyField(Tag)

    