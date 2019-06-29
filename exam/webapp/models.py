from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=256, verbose_name='Полное имя автора')
    date_born = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    date_die = models.DateField(null=True, blank=True, verbose_name='Дата смерти')
    biography = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Биография')
    photo = models.ImageField(upload_to='author_photo', blank=True, null=True, verbose_name="Фотография")

    def __str__(self):
        return f"{self.pk}. {self.name}"
