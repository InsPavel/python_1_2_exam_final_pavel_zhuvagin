from django import forms
from webapp.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['author']
