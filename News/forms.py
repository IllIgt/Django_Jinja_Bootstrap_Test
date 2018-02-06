from django import forms
from .models import Publications, Authors


class PublicationForm(forms.ModelForm):

    class Meta:
        model = Publications
        fields = ('title', 'author', 'date', 'publishing_house', 'location', 'pages')


class AuthorsForm(forms.ModelForm):

    class Meta:
        model = Authors
        fields = ('surname', 'initials', 'is_lab_employee')