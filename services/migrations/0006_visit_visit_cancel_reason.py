# Generated by Django 3.2 on 2021-06-28 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20210628_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='visit_cancel_reason',
            field=models.CharField(blank=True, max_length=200, verbose_name='Причина отмены визита'),
        ),
    ]