# Generated by Django 4.2.11 on 2024-04-08 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_description'),
        ('users', '0002_alter_usuario_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='profiles',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.profile'),
        ),
    ]
