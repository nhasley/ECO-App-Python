# Generated by Django 2.2.4 on 2019-09-19 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_post_published_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user',
            new_name='author',
        ),
    ]
