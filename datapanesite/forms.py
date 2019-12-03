from django import forms
from .models import Entries

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entries
        fields = ["name", "email", "age"]