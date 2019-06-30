from django.contrib import admin
from webapp.models import Author, Book, BookShelf

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookShelf)

