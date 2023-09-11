# Generated by Django 3.2.13 on 2022-07-07 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20220707_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presumptivecasestested',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='presumptivecasestested',
            name='modified_by',
        ),
        migrations.RemoveField(
            model_name='presumptivetestedpositive',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='presumptivetestedpositive',
            name='modified_by',
        ),
        migrations.AlterField(
            model_name='call',
            name='female',
            field=models.CharField(default=0, max_length=25),
        ),
        migrations.AlterField(
            model_name='call',
            name='male',
            field=models.CharField(default=0, max_length=25),
        ),
        migrations.AlterField(
            model_name='caller',
            name='actual_callers',
            field=models.CharField(default=0, max_length=25),
        ),
        migrations.AlterField(
            model_name='caller',
            name='unique_callers',
            field=models.CharField(default=0, max_length=25),
        ),
        migrations.AlterField(
            model_name='detailedcallbreakdown',
            name='abandoned_ivr_after_work',
            field=models.CharField(default=0, max_length=25, verbose_name='Abandoned on IVR After working Hour'),
        ),
        migrations.AlterField(
            model_name='detailedcallbreakdown',
            name='abandoned_ivr_public_holiday',
            field=models.CharField(default=0, max_length=25, verbose_name='Abandoned on IVR on Public Holidays'),
        ),
        migrations.AlterField(
            model_name='detailedcallbreakdown',
            name='abandoned_ivr_weekend',
            field=models.CharField(default=0, max_length=25, verbose_name='Abandoned on IVR on Weekends'),
        ),
        migrations.AlterField(
            model_name='detailedcallbreakdown',
            name='abandoned_ivr_working_hour',
            field=models.CharField(default=0, max_length=25, verbose_name='Abandoned on IVR within Working Hour'),
        ),
        migrations.AlterField(
            model_name='detailedcallbreakdown',
            name='abandoned_welcome_ivr_not_speak',
            field=models.CharField(default=0, max_length=25, verbose_name='Total No. of calls abandoned on welcome IVR and has not indicated to speak with an Agent'),
        ),
        migrations.AlterField(
            model_name='detailedcallbreakdown',
            name='calls_abandoned_agent',
            field=models.CharField(default=0, max_length=25, verbose_name='Total No. of calls abandoned on Agent Queue'),
        ),
        migrations.AlterField(
            model_name='detailedcallbreakdown',
            name='calls_abandoned_ivr_callers',
            field=models.CharField(default=0, max_length=25, verbose_name='Calls abandoned on IVR by Callers'),
        ),
        migrations.AlterField(
            model_name='detailedcallbreakdown',
            name='calls_abandoned_ivr_no_service',
            field=models.CharField(default=0, max_length=25, verbose_name='Calls Abandoned on IVR due to no Service Selection'),
        ),
        migrations.AlterField(
            model_name='detailedcallbreakdown',
            name='calls_abandoned_ivr_wrong_service',
            field=models.CharField(default=0, max_length=25, verbose_name='Calls Abandoned on IVR due to wrong Service Selection'),
        ),
        migrations.AlterField(
            model_name='detailedcallbreakdown',
            name='calls_connected_agent',
            field=models.CharField(default=0, max_length=25, verbose_name='Total No. of calls connected to an Agent'),
        ),
        migrations.AlterField(
            model_name='detailedcallbreakdown',
            name='dropped',
            field=models.CharField(default=0, max_length=25, verbose_name='Dropped'),
        ),
        migrations.AlterField(
            model_name='detailedcallbreakdown',
            name='hoax_call',
            field=models.CharField(default=0, max_length=25, verbose_name='Hoax Calls'),
        ),
        migrations.AlterField(
            model_name='detailedcallbreakdown',
            name='indicate_speak_agent',
            field=models.CharField(default=0, max_length=25, verbose_name='Total No. of Callers that indicated to speak with an Agent'),
        ),
        migrations.AlterField(
            model_name='detailedcallbreakdown',
            name='services_provided_agent',
            field=models.CharField(default=0, max_length=25, verbose_name='TB Services provided by Agent at first call '),
        ),
        migrations.AlterField(
            model_name='detailedcallbreakdown',
            name='test_call',
            field=models.CharField(default=0, max_length=25, verbose_name='Test Calls'),
        ),
        migrations.AlterField(
            model_name='detailedcallbreakdown',
            name='total_self_service_option',
            field=models.CharField(default=0, max_length=25, verbose_name='Total No. of callers that used the Self-Service Option for referral'),
        ),
        migrations.AlterField(
            model_name='reasonnottested',
            name='afraid_stress',
            field=models.CharField(default=0, max_length=25, verbose_name='Afraid of Stress/Not Strong/crowd at the health facility'),
        ),
        migrations.AlterField(
            model_name='reasonnottested',
            name='ask_to_pay',
            field=models.CharField(default=0, max_length=25, verbose_name='I was asked to pay for test'),
        ),
        migrations.AlterField(
            model_name='reasonnottested',
            name='been_busy',
            field=models.CharField(default=0, max_length=25, verbose_name='I have been busy'),
        ),
        migrations.AlterField(
            model_name='reasonnottested',
            name='coughing_anymore',
            field=models.CharField(default=0, max_length=25, verbose_name='Not coughing anymore'),
        ),
        migrations.AlterField(
            model_name='reasonnottested',
            name='coughing_relative',
            field=models.CharField(default=0, max_length=25, verbose_name='I am not the one coughing it was my relative/Friend'),
        ),
        migrations.AlterField(
            model_name='reasonnottested',
            name='locate_address',
            field=models.CharField(default=0, max_length=25, verbose_name='Could not locate the address'),
        ),
        migrations.AlterField(
            model_name='reasonnottested',
            name='no_money',
            field=models.CharField(default=0, max_length=25, verbose_name='No money for card/Transport'),
        ),
        migrations.AlterField(
            model_name='reasonnottested',
            name='not_available',
            field=models.CharField(default=0, max_length=25, verbose_name='Health workers were not available'),
        ),
        migrations.AlterField(
            model_name='reasonnottested',
            name='person_died',
            field=models.CharField(default=0, max_length=25, verbose_name='The person died'),
        ),
        migrations.AlterField(
            model_name='reasonnottested',
            name='relocated',
            field=models.CharField(default=0, max_length=25, verbose_name='Relocated to another state'),
        ),
        migrations.AlterField(
            model_name='reasonnottested',
            name='sputum',
            field=models.CharField(default=0, max_length=25, verbose_name='Could not cough up sputum'),
        ),
        migrations.AlterField(
            model_name='reasonnottested',
            name='therapy',
            field=models.CharField(default=0, max_length=25, verbose_name='On a therapy'),
        ),
        migrations.AlterField(
            model_name='reasonnottested',
            name='tools_testing',
            field=models.CharField(default=0, max_length=25, verbose_name='They do not have tools for testing'),
        ),
        migrations.AlterField(
            model_name='reasonnottested',
            name='travelled',
            field=models.CharField(default=0, max_length=25, verbose_name='I travelled'),
        ),
        migrations.AlterField(
            model_name='referralstatus',
            name='not_referred',
            field=models.CharField(default=0, max_length=25),
        ),
        migrations.AlterField(
            model_name='referralstatus',
            name='referred',
            field=models.CharField(default=0, max_length=25),
        ),
    ]