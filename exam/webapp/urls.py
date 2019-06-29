from django.urls import path
from webapp.views import AuthorListView, AuthorCreateView, AuthorUpdateView, AuthorDetailView, BookListView, BookCreateView, BookUpdateView, BookDetailView

app_name = 'webapp'

urlpatterns = [
    path('author/', AuthorListView.as_view(), name='author_list'),
    path('author/create', AuthorCreateView.as_view(), name="author_create"),
    path('author/<int:pk>/update', AuthorUpdateView.as_view(), name="author_update"),
    path('author/<int:pk>', AuthorDetailView.as_view(), name="author_detail"),
    path('book/', BookListView.as_view(), name="book_list"),
    path('book/create', BookCreateView.as_view(), name="book_create"),
    path('book/<int:pk>/update', BookUpdateView.as_view(), name="book_update"),
    path('book/<int:pk>/detail', BookDetailView.as_view(), name="book_detail"),
]