from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Tag(models.Model):
    captions=models.CharField(max_length=50)

    def __str__(self):
        return self.captions




class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField( max_length=50)
    email_address=models.EmailField(max_length=254)



    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
        


class Post(models.Model):
    title=models.CharField(max_length=100)
    excerpt=models.CharField(max_length=150)
    image=models.CharField(max_length=50)
    date=models.DateField(auto_now=True )
    slug=models.SlugField(unique=True)
    content=models.TextField(validators=[MinLengthValidator(10)])
    author=models.ForeignKey(Author ,  on_delete=models.SET_NULL , null=True ,  related_name="posts")
    tags=models.ManyToManyField(Tag)
