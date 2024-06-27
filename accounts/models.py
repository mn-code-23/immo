from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Utilisateur(AbstractUser):
    pass

class Agent(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    # name_Agency = models.CharField(max_length=180)
    id_Ref = models.CharField(max_length=10)
    tel = models.CharField(max_length=20)
    bio = models.TextField()
    photo = models.ImageField(upload_to="agent", blank=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class Client(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    tel = models.CharField(max_length=20)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

