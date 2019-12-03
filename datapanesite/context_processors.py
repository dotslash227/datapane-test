from django.http import HttpResponse
from .models import Navigation

def NavigationItem(request):
    items = Navigation.objects.all()

    return {"navigation":items}
