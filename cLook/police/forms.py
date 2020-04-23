from django import forms
from .models import *


class AddCriminalForm(forms.ModelForm):
    class Meta:
        model = CriminalDetails
        fields = ['name', 'cid','photo','status']