# Generated by Django 4.1.5 on 2023-01-03 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fmembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('isfamily', models.BooleanField()),
                ('relation', models.CharField(max_length=50)),
            ],
        ),
    ]
