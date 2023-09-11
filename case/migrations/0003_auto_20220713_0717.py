# Generated by Django 3.2.13 on 2022-07-13 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0002_auto_20220707_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='casecategory',
            name='current',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='casestatus',
            name='current',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='casecategory',
            name='non_tb_calls',
            field=models.CharField(default=0, max_length=25, verbose_name='Non-TB Calls'),
        ),
    ]
