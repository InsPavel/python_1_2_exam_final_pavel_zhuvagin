# Generated by Django 2.1 on 2019-06-30 03:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20190630_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookshelf',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_shell', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]