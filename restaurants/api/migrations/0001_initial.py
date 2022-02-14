# Generated by Django 4.0.2 on 2022-02-14 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'restaurant',
                'verbose_name_plural': 'restaurants',
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('cheese', models.CharField(blank=True, max_length=128)),
                ('pastry', models.CharField(blank=True, max_length=128)),
                ('secret_ingredient', models.CharField(blank=True, max_length=128)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizzas', to='api.restaurant')),
            ],
            options={
                'verbose_name': 'pizza',
                'verbose_name_plural': 'pizzas',
            },
        ),
    ]
