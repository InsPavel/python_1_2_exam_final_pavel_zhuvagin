from django import forms
from webapp.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['author']


class UpdateAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['author']
