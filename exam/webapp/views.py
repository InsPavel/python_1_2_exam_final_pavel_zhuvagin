from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from webapp.models import Author, Book, BookShelf, User
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


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'



def book_download(request, pk):
    book = get_object_or_404(Book, pk=pk)
    file = book.file
    file_name = book.file.name
    response = HttpResponse(file, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % file_name
    return response


def soft_delete_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.is_deleted = True
    author.save()
    return redirect('webapp:author_list')


def add_book_to_shelf(request):
    user = request.user
    book_id = request.POST.get('book_id', None)
    book = Book.objects.get(pk=book_id)
    user.user_shell.book.add(book)
    return JsonResponse({'book_object': "Книга добавлена"})


def delete_book_from_shelf(request):
    user = request.user
    book_id = request.POST.get('book_id', None)
    book = Book.objects.get(pk=book_id)
    user.user_shell.book.remove(book)
    return JsonResponse({'book_object': "Книга удалена"})