# Generated by Django 2.2.4 on 2019-09-13 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_remove_challenge_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='description',
        ),
        migrations.RemoveField(
            model_name='challenge',
            name='name',
        ),
        migrations.RemoveField(
            model_name='challenge',
            name='points',
        ),
        migrations.AddField(
            model_name='challenge',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]