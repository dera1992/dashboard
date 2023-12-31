# Generated by Django 3.2.13 on 2022-07-07 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_auto_20220707_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeographicalDistribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('north_west', models.CharField(max_length=50)),
                ('north_east', models.CharField(max_length=50)),
                ('north_central', models.CharField(max_length=50)),
                ('south_south', models.CharField(max_length=50)),
                ('south_east', models.CharField(max_length=50)),
                ('south_west', models.CharField(max_length=50)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='geographical_geographicaldistribution_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='geographical_geographicaldistribution_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Geographical Distribution',
                'verbose_name_plural': 'Geographical Distribution',
            },
        ),
        migrations.CreateModel(
            name='GenderGeographical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='geographical_gendergeographical_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='geographical_gendergeographical_updated_by', to=settings.AUTH_USER_MODEL)),
                ('north_central', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='north_central', to='home.call')),
                ('north_east', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='north_east', to='home.call')),
                ('north_west', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='north_west', to='home.call')),
                ('south_east', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='south_east', to='home.call')),
                ('south_south', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='south_south', to='home.call')),
                ('south_west', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='south_west', to='home.call')),
            ],
            options={
                'verbose_name': 'Gender by Geopolitical Zones',
                'verbose_name_plural': 'Gender by Geopolitical Zones',
            },
        ),
    ]
