import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from slugify import slugify
from PIL import Image
import random
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=False, default='First')
    last_name = models.CharField(max_length=30, blank=False, default='Last')
    email = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}Profile'


    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Post(models.Model):
    user= models.CharField(max_length=100)
    title= models.CharField(max_length=100)
    content= models.TextField()
    category = models.CharField(max_length=30, default='others')
    url= models.SlugField(max_length=100, unique=False, blank=True, editable=False)

    def save(self, *args, **kwargs):
        randoms = str(random.randint(0, 100))
        randoms2 = str(random.randint(200, 1000))
        self.url= randoms2+self.title.split(' ')[0]+randoms
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
