from leads.models import Leads
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = Leads
        fields = '__all__'