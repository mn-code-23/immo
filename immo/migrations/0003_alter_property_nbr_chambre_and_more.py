# Generated by Django 5.0 on 2024-05-30 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immo', '0002_property_desc_alter_property_nbr_chambre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='nbr_chambre',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='nbr_salle_bain',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
