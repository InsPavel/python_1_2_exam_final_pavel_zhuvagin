# Generated by Django 2.1 on 2019-06-30 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0005_auto_20190629_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookShelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='bookshelf',
            name='book',
            field=models.ManyToManyField(related_name='book', to='webapp.Book', verbose_name='Книги'),
        ),
        migrations.AddField(
            model_name='bookshelf',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
