# Generated by Django 3.2.13 on 2022-07-07 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_auto_20220602_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('actual_callers', models.CharField(max_length=30)),
                ('unique_callers', models.CharField(max_length=30)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='home_caller_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='home_caller_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Caller',
                'verbose_name_plural': 'Callers',
            },
        ),
        migrations.CreateModel(
            name='DetailedCallBreakdown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('total_self_service_option', models.CharField(max_length=50, verbose_name='Total No. of callers that used the Self-Service Option for referral')),
                ('indicate_speak_agent', models.CharField(max_length=50, verbose_name='Total No. of Callers that indicated to speak with an Agent')),
                ('services_provided_agent', models.CharField(max_length=50, verbose_name='TB Services provided by Agent at first call ')),
                ('dropped', models.CharField(max_length=50, verbose_name='Dropped')),
                ('hoax_call', models.CharField(max_length=50, verbose_name='Hoax Calls')),
                ('test_call', models.CharField(max_length=50, verbose_name='Test Calls')),
                ('calls_connected_agent', models.CharField(max_length=50, verbose_name='Total No. of calls connected to an Agent')),
                ('calls_abandoned_agent', models.CharField(max_length=50, verbose_name='Total No. of calls abandoned on Agent Queue')),
                ('abandoned_ivr_working_hour', models.CharField(max_length=50, verbose_name='Abandoned on IVR within Working Hour')),
                ('abandoned_ivr_after_work', models.CharField(max_length=50, verbose_name='Abandoned on IVR After working Hour')),
                ('abandoned_ivr_public_holiday', models.CharField(max_length=50, verbose_name='Abandoned on IVR on Public Holidays')),
                ('abandoned_ivr_weekend', models.CharField(max_length=50, verbose_name='Abandoned on IVR on Weekends')),
                ('abandoned_welcome_ivr_not_speak', models.CharField(max_length=50, verbose_name='Total No. of calls abandoned on welcome IVR and has not indicated to speak with an Agent')),
                ('calls_abandoned_ivr_callers', models.CharField(max_length=50, verbose_name='Calls abandoned on IVR by Callers')),
                ('calls_abandoned_ivr_wrong_service', models.CharField(max_length=50, verbose_name='Calls Abandoned on IVR due to wrong Service Selection')),
                ('calls_abandoned_ivr_no_service', models.CharField(max_length=50, verbose_name='Calls Abandoned on IVR due to no Service Selection')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='home_detailedcallbreakdown_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='home_detailedcallbreakdown_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Detailed Call Breakdown',
                'verbose_name_plural': 'Detailed Call Breakdown',
            },
        ),
        migrations.CreateModel(
            name='ReasonNotTested',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('relocated', models.CharField(max_length=50, verbose_name='Relocated to another state')),
                ('not_available', models.CharField(max_length=50, verbose_name='Health workers were not available')),
                ('been_busy', models.CharField(max_length=50, verbose_name='I have been busy')),
                ('coughing_anymore', models.CharField(max_length=50, verbose_name='Not coughing anymore')),
                ('ask_to_pay', models.CharField(max_length=50, verbose_name='I was asked to pay for test')),
                ('sputum', models.CharField(max_length=50, verbose_name='Could not cough up sputum')),
                ('locate_address', models.CharField(max_length=50, verbose_name='Could not locate the address')),
                ('tools_testing', models.CharField(max_length=50, verbose_name='They do not have tools for testing')),
                ('coughing_relative', models.CharField(max_length=50, verbose_name='I am not the one coughing it was my relative/Friend')),
                ('travelled', models.CharField(max_length=50, verbose_name='I travelled')),
                ('therapy', models.CharField(max_length=50, verbose_name='On a therapy')),
                ('no_money', models.CharField(max_length=50, verbose_name='No money for card/Transport')),
                ('person_died', models.CharField(max_length=50, verbose_name='The person died')),
                ('afraid_stress', models.CharField(max_length=50, verbose_name='Afraid of Stress/Not Strong/crowd at the health facility')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='home_reasonnottested_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='home_reasonnottested_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reasons for not getting tested by States',
                'verbose_name_plural': 'Reasons for not getting tested by States',
            },
        ),
        migrations.CreateModel(
            name='ReferralStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('referred', models.CharField(max_length=50)),
                ('not_referred', models.CharField(max_length=50)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='home_referralstatus_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='home_referralstatus_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Referral Status',
                'verbose_name_plural': 'Referral Status',
            },
        ),
        migrations.RemoveField(
            model_name='casestatus',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='casestatus',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='genderdistribution',
            name='calls',
        ),
        migrations.RemoveField(
            model_name='genderdistribution',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='genderdistribution',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='genderdistribution',
            name='presumptive_cases_tested',
        ),
        migrations.RemoveField(
            model_name='genderdistribution',
            name='presumptive_tested_positive',
        ),
        migrations.RemoveField(
            model_name='geographicaldistribution',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='geographicaldistribution',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='inboundstatistics',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='inboundstatistics',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='languageselection',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='languageselection',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='sourcehotlineinformation',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='sourcehotlineinformation',
            name='modified_by',
        ),
        migrations.DeleteModel(
            name='CaseCategory',
        ),
        migrations.DeleteModel(
            name='CaseStatus',
        ),
        migrations.DeleteModel(
            name='GenderDistribution',
        ),
        migrations.DeleteModel(
            name='GeographicalDistribution',
        ),
        migrations.DeleteModel(
            name='InboundStatistics',
        ),
        migrations.DeleteModel(
            name='LanguageSelection',
        ),
        migrations.DeleteModel(
            name='SourceHotlineInformation',
        ),
    ]
