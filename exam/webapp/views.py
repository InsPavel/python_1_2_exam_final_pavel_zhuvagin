from django.shortcuts import render
from django.views.generic import ListView
from webapp.models import Author
from django.views.generic.base import TemplateView


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
