from django.shortcuts import render, get_object_or_404

from immo.models import Property


# Create your views here.

def index(request):
    bien = Property.objects.all()[:3]
    house = Property.objects.filter(property_type="Maison")
    villa = Property.objects.filter(property_type="Villa")
    terrain = Property.objects.filter(property_type="Terrain")
    appartement = Property.objects.filter(property_type="Appartement")
    return render(request, "index.html", context={"bien": bien, "house": house, "villa": villa, "terrain": terrain, "appartement": appartement})

def detail(request, id):
    property = get_object_or_404(Property, id=id)
    item_type = property.property_type
    property_relation = Property.objects.filter(property_type=item_type)[:3]
    item_name = request.GET.get('item_name')
    if item_name != "" and item_name is not None:
        property_relation = Property.objects.filter(slug=item_name)[:2]
    return render(request, "detail.html", context={"property": property, "property_relation": property_relation})

def maisonAV(request):
    house = Property.objects.filter(property_type="Maison", status="Vendre")
    return render(request, "maison.html", context={"house": house})

def maisonLou(request):
    house = Property.objects.filter(property_type="Maison", status="Louer")
    return render(request, "maisonLou.html", context={"house": house})


def terrain(request):
    terrain = Property.objects.filter(property_type="Terrain", status="Vendre")
    return render(request, "terrain.html", context={"terrain": terrain})

def appartementAV(request):
    appartement = Property.objects.filter(property_type="Appartement", status="Vendre")
    return render(request, "appartement.html", context={"appartement": appartement})

def appartementLou(request):
    appartement = Property.objects.filter(property_type="Appartement", status="Louer")
    return render(request, "appartementLou.html", context={"appartement": appartement})