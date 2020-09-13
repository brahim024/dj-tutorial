# Generated by Django 3.1 on 2020-09-13 11:40

from django.db import migrations, models
import myapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='headshot',
        ),
        migrations.AddField(
            model_name='author',
            name='headshot',
            field=models.ImageField(default='', upload_to=myapp.models.author_headshots),
            preserve_default=False,
        ),
    ]