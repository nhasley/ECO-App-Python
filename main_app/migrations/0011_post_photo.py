# Generated by Django 2.2.4 on 2019-09-16 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20190916_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
