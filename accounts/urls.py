from django.urls import path

from accounts.views import login_user, signup, logout_user, profil, agent

urlpatterns = [
    path('accounts/login/', login_user, name="login"),
    path('accounts/signup/', signup, name="signup"),
    path('accounts/logout/', logout_user, name="logout"),
    path('accounts/profil/', profil, name="profil"),
    path('Agent Immobilier/', agent, name="agent"),
]