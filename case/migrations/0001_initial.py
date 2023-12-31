# Generated by Django 3.2.13 on 2022-07-07 09:54

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
            name='CaseStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('open', models.CharField(max_length=50)),
                ('escalated', models.CharField(max_length=50)),
                ('pending', models.CharField(max_length=50)),
                ('resolved', models.CharField(max_length=50)),
                ('resolved_closed', models.CharField(max_length=50)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='case_casestatus_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='case_casestatus_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Case Status',
                'verbose_name_plural': 'Case Status',
            },
        ),
        migrations.CreateModel(
            name='CaseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('inquiry_for_information', models.CharField(max_length=50)),
                ('inquiry_for_service', models.CharField(max_length=50)),
                ('hoax_call', models.CharField(max_length=50)),
                ('non_tb_calls', models.CharField(max_length=50, verbose_name='Non-TB Calls')),
                ('appreciation_acknowledgement', models.CharField(max_length=50, verbose_name='Appreciation/Acknowledgement')),
                ('service_complaint', models.CharField(max_length=50)),
                ('technical_complaint', models.CharField(max_length=50)),
                ('covid_19', models.CharField(max_length=50, verbose_name='Covid-19')),
                ('suggestions', models.CharField(max_length=50)),
                ('dropped_calls', models.CharField(max_length=50)),
                ('test_calls', models.CharField(max_length=50)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='case_casecategory_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='case_casecategory_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Case Category',
                'verbose_name_plural': 'Case Categories',
            },
        ),
    ]
