# Generated by Django 5.0 on 2024-05-29 20:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_agent_id_ref_client'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_type', models.CharField(max_length=50)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('nbr_chambre', models.IntegerField()),
                ('nbr_salle_bain', models.IntegerField()),
                ('price', models.IntegerField()),
                ('address', models.CharField(max_length=180)),
                ('city', models.CharField(max_length=180)),
                ('region', models.CharField(max_length=180)),
                ('status', models.CharField(max_length=10)),
                ('image', models.ImageField(blank=True, upload_to='property')),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('agent_Ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.agent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
