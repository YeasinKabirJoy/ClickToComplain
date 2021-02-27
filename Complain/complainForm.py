from django import forms
from .models import Complain
from tagContactFAQ.models import Tag

class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ('image', 'description','tag', 'private')
        widgets = {
            'tag':forms.CheckboxSelectMultiple()
        }

