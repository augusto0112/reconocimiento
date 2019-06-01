from django.db import models

# Create your models here.

class Blog(models.Model):
    Title = models.CharField(max_length=100)
    Image = models.ImageField()
    Content = models.CharField(max_length=1000)
    Tag = models.CharField(max_length=100)
    Slug = models.SlugField(max_length=200, unique=True)
    Date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.Title