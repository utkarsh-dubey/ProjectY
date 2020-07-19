import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from slugify import slugify

# Create your models here.


class Post(models.Model):
    user= models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    title= models.CharField(max_length=500)
    content= models.TextField()
    url= models.SlugField(max_length=500, unique=False, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.url= self.title
        super(Post, self).save(*args, **kwargs)