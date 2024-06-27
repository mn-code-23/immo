from django.db import models
from numpy.lib.recfunctions import require_fields

from accounts.models import Agent
from mn_immo.settings import AUTH_USER_MODEL


# Create your models here.

class Property (models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    property_type  = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    width = models.IntegerField()
    height = models.IntegerField()
    nbr_chambre = models.IntegerField(blank=True, null=True)
    nbr_salle_bain = models.IntegerField(blank=True, null=True)
    price = models.IntegerField()
    address = models.CharField(max_length=180)
    city = models.CharField(max_length =180)
    region = models.CharField(max_length=180)
    status = models.CharField(max_length=10)
    agent_Ref = models.ForeignKey(Agent, on_delete=models.CASCADE)
    desc = models.TextField()
    image = models.ImageField(upload_to="property", blank=True)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} ({self.property_type})"
