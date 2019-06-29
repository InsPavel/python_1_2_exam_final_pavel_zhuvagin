from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from webapp.models import Author, Book
from webapp.forms import AuthorForm, UpdateAuthorForm, BookForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404


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

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            return redirect('webapp:author_list')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:author_detail', kwargs={'pk': self.object.pk})


class AuthorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Author
    form_class = UpdateAuthorForm
    template_name = 'author_update.html'
    permission_required = 'webapp'

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            return redirect('webapp:author_list')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:author_detail', kwargs={'pk': self.object.pk})


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_create.html'
    permission_required = 'webapp.add_book'

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            return redirect('webapp:author_list')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:book_detail', kwargs={'pk': self.object.pk})


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_update.html'
    permission_required = 'webapp.book_update'

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            return redirect('webapp:author_list')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:book_detail', kwargs={'pk': self.object.pk})


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_delete.html'
    permission_required = 'webapp.book_delete'

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            return redirect('webapp:author_list')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:book_list')


def book_download(request, pk):
    book = get_object_or_404(Book, pk=pk)
    file = book.file
    file_name = book.file.name
    response = HttpResponse(file, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % file_name
    return response