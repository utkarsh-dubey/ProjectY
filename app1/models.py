import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from slugify import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=False, default='First')
    last_name = models.CharField(max_length=30, blank=False, default='Last')
    email = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username}Profile'    

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Post(models.Model):
    user= models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    title= models.CharField(max_length=500)
    content= models.TextField()
    url= models.SlugField(max_length=500, unique=False, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.url= self.title
        super(Post, self).save(*args, **kwargs)
