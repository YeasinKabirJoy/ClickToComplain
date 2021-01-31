from django import forms
from .models import Complain

class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ('image', 'description', 'private')