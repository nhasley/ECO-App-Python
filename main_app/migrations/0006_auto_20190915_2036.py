# Generated by Django 2.2.4 on 2019-09-15 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20190915_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('challenge', models.CharField(choices=[('M', 'Metro'), ('B', 'Bike'), ('W', 'Walk')], default='M', max_length=1)),
            ],
        ),
        migrations.DeleteModel(
            name='Challenge',
        ),
    ]
