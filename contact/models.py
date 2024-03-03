from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse
# Create your models here.

# contact model
class Contact (models.Model):
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    message = models.TextField(max_length=500, null=True)

    def __str__(self):
        return '{}'.format(self.firstname)

#profile model   
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    # Add more fields as needed

    def __str__(self):
        return self.user.username
    
# Create or update a user's profile
# @receiver(post_save, sender=User)

#update profile
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
