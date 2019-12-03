from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.Home, name="home"),    
    path('entries/add', views.Entries.as_view(), name="entry"),
    path('entries', views.EntryPage, name="entry-index"),
]