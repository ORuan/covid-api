from leads.models import Leads
from django.forms import ModelForm

class UserForm(ModelForm):
    class meta:
        model = Leads
        fields = "__all__"