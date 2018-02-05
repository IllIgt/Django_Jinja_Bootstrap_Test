from django import forms
from .models import Publications


class PublicationForm(forms.ModelForm):

    class Meta:
        model = Publications
        fields = ('title', 'author', 'date', 'publishing_house', 'location', 'pages')

