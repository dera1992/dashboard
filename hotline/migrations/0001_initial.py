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
            name='SourceHotlineInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('radio', models.CharField(max_length=50)),
                ('tv', models.CharField(max_length=50)),
                ('friends_family', models.CharField(max_length=50)),
                ('handbill_posters', models.CharField(max_length=50)),
                ('sms', models.CharField(max_length=50)),
                ('training_and_campaign', models.CharField(max_length=50)),
                ('facebook_twitter_instagram', models.CharField(max_length=50)),
                ('schools', models.CharField(max_length=50)),
                ('ppmvs', models.CharField(max_length=50)),
                ('religious_settings', models.CharField(max_length=50)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hotline_sourcehotlineinformation_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hotline_sourcehotlineinformation_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Source Hotline Information',
                'verbose_name_plural': 'Source Hotline Information',
            },
        ),
    ]
