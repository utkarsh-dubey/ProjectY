import datetime
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from slugify import slugify
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

<<<<<<< HEAD
<<<<<<< HEAD

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


=======
>>>>>>> parent of b5dd82a... Merge branch 'master' of https://github.com/utkarsh-dubey/ProjectY
=======
>>>>>>> parent of b5dd82a... Merge branch 'master' of https://github.com/utkarsh-dubey/ProjectY
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Post(models.Model):
    user= models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    title= models.CharField(max_length=100)
    content= models.TextField()
    category = models.CharField(max_length=30, default='others')
    url= models.SlugField(max_length=100, unique=False, blank=True, editable=False)

    def save(self, *args, **kwargs):
        randoms = str(random.randint(0, 100))
        randoms2 = str(random.randint(200, 1000))
        self.url= randoms2+self.title.split(' ')[0]+randoms
        super(Post, self).save(*args, **kwargs)
