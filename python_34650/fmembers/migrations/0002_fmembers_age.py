# Generated by Django 4.1.5 on 2023-01-04 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmembers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fmembers',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]