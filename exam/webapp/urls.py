from django.urls import path
from webapp.views import AuthorListView, AuthorCreateView, AuthorUpdateView, AuthorDetailView, BookListView, BookCreateView, BookUpdateView, BookDetailView, BookDeleteView, book_download, soft_delete_author, UserDetailView, UserListView

app_name = 'webapp'

urlpatterns = [
    path('', BookListView.as_view(), name="book_list"),
    path('author/', AuthorListView.as_view(), name='author_list'),
    path('author/create', AuthorCreateView.as_view(), name="author_create"),
    path('author/<int:pk>/update', AuthorUpdateView.as_view(), name="author_update"),
    path('author/<int:pk>', AuthorDetailView.as_view(), name="author_detail"),
    path('book/<int:pk>/delete', soft_delete_author, name='author_delete'),
    path('book/create', BookCreateView.as_view(), name="book_create"),
    path('book/<int:pk>/update', BookUpdateView.as_view(), name="book_update"),
    path('book/<int:pk>/detail', BookDetailView.as_view(), name="book_detail"),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name="book_delete"),
    path('book/<int:pk>/download', book_download, name='book_download'),
    path('user/list', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>/detail', UserDetailView.as_view(), name='user_detail'),
]