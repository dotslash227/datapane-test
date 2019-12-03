from django.shortcuts import render
from django.views import View
from .forms import EntryForm
from django.contrib import messages
from .models import Entries as EntryModel

# Home View
def Home(request):
    return render(request, "index.html", {})


# Page for viewing entry
def EntryPage(request):
    data = EntryModel.objects.all()

    return render(request, "entries/index.html", {
        "data": data
    })


# Base page for  rendering the csv upload form
def csvView(request):
    return render(request, "csv.html", {})



# Class based view for showing entry form and handling post mehtod
class Entries(View):    
    def get(self, request):
        form = EntryForm()

        return render(request, "entries/add.html", {
            "form": form
        })

    def post(self, request):
        form = EntryForm(request.POST)
        if form.is_valid():
            # Try to save form, send to  form if error found and show a message. Not doing exception handling right now
            try:
                form.save()
            except:
                messages.add_message(request, messages.SUCESS, "Your form has erorrs")                
                return render(request, "entries/add.html", {
                    "form": form
                })
            else:
                messages.add_message(request, messages.SUCCESS, "Your entry has been saved")        
                data = EntryModel.objects.all() 
                
                return render(request, "entries/index.html", {
                    "data":data
                })               