# Generated by Django 2.2.4 on 2019-09-19 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_auto_20190919_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user',
        ),
    ]
