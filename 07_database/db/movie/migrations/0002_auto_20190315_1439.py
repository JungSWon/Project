# Generated by Django 2.1.7 on 2019-03-15 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='score',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='score',
            name='updated_at',
        ),
    ]