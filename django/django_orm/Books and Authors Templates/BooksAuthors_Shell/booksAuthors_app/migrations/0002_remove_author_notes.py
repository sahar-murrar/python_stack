# Generated by Django 2.2.4 on 2021-05-23 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booksAuthors_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='notes',
        ),
    ]