from leads.models import Leads
from django.forms import ModelForm
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = Leads
        fields = ['number', 'city']

        widgets = {
            'number': forms.NumberInput(attrs={'class':'validate', 'placeholder':'5577998714634', 'id':"number" }),
        }