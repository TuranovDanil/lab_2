# Generated by Django 4.1.1 on 2022-11-29 10:57

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookFile',
            field=models.FileField(null=True, upload_to='media/books', verbose_name='Файл с книгой'),
        ),
        migrations.AlterField(
            model_name='book',
            name='photoPreview',
            field=models.ImageField(null=True, upload_to='media/cover', validators=[api.models.Book.validate_image], verbose_name='Изображения'),
        ),
    ]
