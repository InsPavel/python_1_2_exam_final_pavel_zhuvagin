from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=256, verbose_name='Полное имя автора')
    date_born = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    date_die = models.DateField(null=True, blank=True, verbose_name='Дата смерти')
    biography = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Биография')
    photo = models.ImageField(upload_to='author_photo', blank=True, null=True, verbose_name="Фотография")
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название книги')
    author = models.ForeignKey(Author, verbose_name='Автор', related_name='book', on_delete=models.CASCADE)
    publication = models.TextField(max_length=10, verbose_name='Год издания')
    file = models.FileField(upload_to='book_file', blank=True, null=True, verbose_name="Файл с текстом")
    image = models.ImageField(upload_to='book_photo', blank=True, null=True, verbose_name="Обложка")
    description = models.TextField(max_length=1000, blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return f"{self.pk}. {self.name}"


class BookShelf(models.Model):
    user = models.OneToOneField(User, related_name='user_shell',  verbose_name='Пользователь', on_delete=models.CASCADE)
    book = models.ManyToManyField('Book', related_name='book', verbose_name='Книги')

    def __str__(self):
        return f"{self.user} {self.user.pk}"

