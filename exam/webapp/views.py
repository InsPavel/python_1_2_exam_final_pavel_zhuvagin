from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from webapp.models import Author
from webapp.forms import AuthorForm, UpdateAuthorForm
from django.views.generic.base import TemplateView


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_create.html'

    def get_success_url(self):
        return reverse('author_detail', kwargs={'pk': self.object.pk})


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = UpdateAuthorForm
    template_name = 'author_update.html'

    def get_success_url(self):
        return reverse('author_detail', kwargs={'pk': self.object.pk})

