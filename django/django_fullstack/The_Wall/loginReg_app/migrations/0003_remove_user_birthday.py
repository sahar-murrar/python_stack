# Generated by Django 2.2.4 on 2021-05-26 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginReg_app', '0002_user_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
    ]
