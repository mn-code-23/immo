from django.urls import path
from .views import index, detail, maisonAV, maisonLou, appartementAV, appartementLou, terrain

urlpatterns = [
    path('', index, name="index"),
    path('detail/<int:id>/', detail, name="detail"),
    path('maison/vendre/', maisonAV, name="maisonAV"),
    path('maison/Louer/', maisonLou, name="maisonLou"),
    path('appartement/vendre/', appartementAV, name="appartementAV"),
    path('appartement/Louer/', appartementLou, name="appartementLou"),
    path('terrain/Vendre/', terrain, name="terrain"),
]