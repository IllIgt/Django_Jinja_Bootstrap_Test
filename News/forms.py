from django import forms
from .models import Publications


class PublicationForm(forms.ModelForm):

    class Meta:
        model = Publications
        fields = ('title', 'text')
