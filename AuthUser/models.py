from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, default='avatars/avatarImg.jpg')
    bio = models.TextField(max_length=500, blank=True)


    def __str__(self):
        return self.user.username
