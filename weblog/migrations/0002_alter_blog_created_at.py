# Generated by Django 5.1.5 on 2025-02-09 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
