from django import forms
from webapp.models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['author']


class UpdateAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ['author']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['book']
