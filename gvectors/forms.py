from django import forms
from .models import GVector

class GVectorForm(forms.ModelForm):
    class Meta:
        model = GVector
        fields = ('description', 'gvector', )