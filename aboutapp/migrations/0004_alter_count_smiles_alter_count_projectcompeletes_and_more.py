# Generated by Django 5.1.5 on 2025-02-09 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutapp', '0003_count_smiles_count_projectcompeletes_count_years'),
    ]

    operations = [
        migrations.AlterField(
            model_name='count',
            name='Smiles',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='count',
            name='projectCompeletes',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='count',
            name='years',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
