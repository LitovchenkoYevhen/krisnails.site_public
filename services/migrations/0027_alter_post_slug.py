# Generated by Django 3.2 on 2021-07-06 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0026_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='URL'),
        ),
    ]