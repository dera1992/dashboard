# Generated by Django 3.2.13 on 2022-07-07 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languageselection',
            name='english',
            field=models.CharField(default=0, max_length=25),
        ),
        migrations.AlterField(
            model_name='languageselection',
            name='hausa',
            field=models.CharField(default=0, max_length=25),
        ),
        migrations.AlterField(
            model_name='languageselection',
            name='igbo',
            field=models.CharField(default=0, max_length=25),
        ),
        migrations.AlterField(
            model_name='languageselection',
            name='pidgin',
            field=models.CharField(default=0, max_length=25),
        ),
        migrations.AlterField(
            model_name='languageselection',
            name='yoruba',
            field=models.CharField(default=0, max_length=25),
        ),
    ]