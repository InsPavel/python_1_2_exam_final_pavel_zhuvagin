from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView
from webapp.models import Author
from webapp.forms import AuthorForm
from django.views.generic.base import TemplateView


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_create.html'

    # def get_success_url(self):
    #     return reverse('webapp:post_detail', kwargs={'pk': self.object.pk})

