# Generated by Django 2.2.4 on 2019-09-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0023_auto_20190920_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
