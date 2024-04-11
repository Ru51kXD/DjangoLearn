from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='avatars', null=True, blank=True)
    
class Task(models.Model):
    title = models.CharField('Named',max_length=50)
    task = models.TextField()