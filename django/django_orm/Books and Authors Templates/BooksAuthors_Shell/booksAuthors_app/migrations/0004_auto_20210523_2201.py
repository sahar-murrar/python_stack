# Generated by Django 2.2.4 on 2021-05-23 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksAuthors_app', '0003_author_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(related_name='authors', to='booksAuthors_app.Books'),
        ),
    ]
