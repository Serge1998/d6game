# Generated by Django 4.2.11 on 2025-07-20 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Partie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField(unique=True)),
                ('joueur_tour1', models.PositiveIntegerField()),
                ('joueur_tour2', models.PositiveIntegerField()),
                ('croupier_tour1', models.PositiveIntegerField()),
                ('croupier_tour2', models.PositiveIntegerField()),
                ('date_debut', models.DateTimeField(auto_now_add=True)),
                ('date_fin', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Téléphone')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Pays')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
