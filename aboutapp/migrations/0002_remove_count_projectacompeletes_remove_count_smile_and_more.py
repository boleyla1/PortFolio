# Generated by Django 5.1.5 on 2025-02-09 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='count',
            name='ProjectaCompeletes',
        ),
        migrations.RemoveField(
            model_name='count',
            name='Smile',
        ),
        migrations.RemoveField(
            model_name='count',
            name='years',
        ),
    ]
