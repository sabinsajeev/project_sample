from  django import forms
from .models import dispmodel

class appfrom(forms.ModelForm):
    class Meta:
        model = dispmodel
        fields=[
            "title",
            "description",
        ]