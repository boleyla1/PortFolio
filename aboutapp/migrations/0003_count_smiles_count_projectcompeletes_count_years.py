# Generated by Django 5.1.5 on 2025-02-09 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutapp', '0002_remove_count_projectacompeletes_remove_count_smile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='count',
            name='Smiles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='count',
            name='projectCompeletes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='count',
            name='years',
            field=models.IntegerField(default=0),
        ),
    ]
