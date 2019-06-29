from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from webapp.models import Author, Book
from webapp.forms import AuthorForm, UpdateAuthorForm, BookForm
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
        return reverse('webapp:author_detail', kwargs={'pk': self.object.pk})


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    form_class = UpdateAuthorForm
    template_name = 'author_update.html'
    permission_required = 'webapp'

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('webapp:author_detail', kwargs={'pk': self.object.pk})


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_create.html'
    permission_required = 'webapp.add_book'

    def get_success_url(self):
        return reverse('webapp:book_detail', kwargs={'pk': self.object.pk})


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_update.html'
    permission_required = 'webapp.book_update'

    def get_permission_required(self):
        return None

    def has_permission(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return reverse('webapp:book_detail', kwargs={'pk': self.object.pk})
