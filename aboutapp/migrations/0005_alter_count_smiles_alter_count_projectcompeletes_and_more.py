# Generated by Django 5.1.5 on 2025-02-09 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutapp', '0004_alter_count_smiles_alter_count_projectcompeletes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='count',
            name='Smiles',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='count',
            name='projectCompeletes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='count',
            name='years',
            field=models.IntegerField(default=0),
        ),
    ]
