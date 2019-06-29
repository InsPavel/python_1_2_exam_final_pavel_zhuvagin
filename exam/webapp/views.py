from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from webapp.models import Author
from webapp.forms import AuthorForm, UpdateAuthorForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'


class AuthorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author_create.html'
    permission_required = 'webapp.add_author'

    def get_success_url(self):
        return reverse('author_detail', kwargs={'pk': self.object.pk})


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    form_class = UpdateAuthorForm
    template_name = 'author_update.html'
    permission_required = 'webapp'

    def get_success_url(self):
        return reverse('author_detail', kwargs={'pk': self.object.pk})


