# Generated by Django 4.2.11 on 2024-05-31 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_clients_veiculos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='veiculos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.vehicle', verbose_name='Perfis:'),
        ),
    ]
