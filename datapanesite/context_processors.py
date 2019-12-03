from django.http import HttpResponse
from .models import Navigation


# Dynamic menu items
def NavigationItem(request):
    items = Navigation.objects.all()

    return {"navigation":items}
