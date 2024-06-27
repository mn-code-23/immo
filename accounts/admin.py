from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Utilisateur, Agent, Client
# Register your models here.

admin.site.register(Utilisateur, UserAdmin)
admin.site.register(Agent)
admin.site.register(Client)
