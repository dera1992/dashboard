# Generated by Django 3.2.13 on 2022-07-07 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presumptive', '0002_auto_20220707_1225'),
        ('home', '0006_auto_20220707_1225'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PresumptiveCasesTested',
        ),
        migrations.DeleteModel(
            name='PresumptiveTestedPositive',
        ),
    ]
