from django.db import models

from django.utils import timezone

# Create your models here.



class Post(models.Model):
    auther = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    created_date = models.DateTimeField(default = timezone.now)
    content = models.TextField(max_length=200000)
    #love = models.ManyToManyField()
    #unicorn = models.ManyToManyField()


    def __str__(self):
        return self.title

    

