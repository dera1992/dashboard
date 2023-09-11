from import_export import resources
from import_export.fields import Field
from .models import ReferralStatus, DetailedCallBreakdown, ReasonNotTested


class ReferralStatusResource(resources.ModelResource):
    id = Field(attribute='id', column_name='Id')
    referred = Field(attribute='referred', column_name='Referred')
    not_referred = Field(attribute='not_referred', column_name='Not Referred')

    class Meta:
        model = ReferralStatus
        fields = ('id', 'referred', 'not_referred')

class DetailedCallBreakdownResource(resources.ModelResource):
     id = Field(attribute='id', column_name='Id')
     total_self_service_option = Field(attribute='total_self_service_option', column_name='Total No. of callers that used the Self-Service Option for referral')
     indicate_speak_agent = Field(attribute='indicate_speak_agent ', column_name='Total No. of Callers that indicated to speak with an Agent')
     services_provided_agent = Field(attribute='services_provided_agent', column_name='TB Services provided by Agent at first call')
     dropped = Field(attribute='dropped', column_name='Dropped')
     hoax_call = Field(attribute='hoax_call', column_name='Hoax Calls')
     test_call = Field(attribute='test_call', column_name='Test Calls')
     calls_connected_agent = Field(attribute='calls_connected_agent', column_name='Total No. of calls connected to an AgentReferred')
     calls_abandoned_agent = Field(attribute='calls_abandoned_agent', column_name='Total No. of calls abandoned on Agent Queue')
     abandoned_ivr_working_hour = Field(attribute='abandoned_ivr_working_hour', column_name='Abandoned on IVR within Working Hour')
     abandoned_ivr_after_work = Field(attribute='abandoned_ivr_after_work', column_name='Abandoned on IVR After working Hour')
     abandoned_ivr_public_holiday = Field(attribute='abandoned_ivr_public_holiday', column_name='Abandoned on IVR on Public Holidays')
     abandoned_ivr_weekend = Field(attribute='abandoned_ivr_weekend', column_name='Abandoned on IVR on Weekends')
     abandoned_welcome_ivr_not_speak = Field(attribute='abandoned_welcome_ivr_not_speak', column_name='Total No. of calls abandoned on welcome IVR and has not indicated to speak with an Agent')
     calls_abandoned_ivr_callers = Field(attribute='calls_abandoned_ivr_callers', column_name='Calls abandoned on IVR by Callers')
     calls_abandoned_ivr_wrong_service = Field(attribute='calls_abandoned_ivr_wrong_service', column_name='Calls Abandoned on IVR due to wrong Service Selection')
     calls_abandoned_ivr_no_service = Field(attribute='calls_abandoned_ivr_no_service', column_name='Calls Abandoned on IVR due to no Service Selection')
     not_referred = Field(attribute='not_referred', column_name='Not Referred')

     class Meta:
         model = DetailedCallBreakdown
         exclude = ('is_active','modified_at','created_by','created_at','modified_by' )


class ReasonNotTestedResource(resources.ModelResource):
    id = Field(attribute='id', column_name='Id')
    relocated = Field(attribute='relocated',column_name='Relocated to another state')
    not_available = Field(attribute='not_available',column_name='Health workers were not available')
    been_busy = Field(attribute='been_busy',column_name='I have been busy')
    coughing_anymore = Field(attribute='coughing_anymore', column_name='Not coughing anymore')
    ask_to_pay = Field(attribute='ask_to_pay', column_name='I was asked to pay for test')
    sputum = Field(attribute='sputum', column_name='Could not cough up sputum')
    locate_address = Field(attribute='locate_address',
                                  column_name='Could not locate the address')
    tools_testing = Field(attribute='tools_testing',
                                  column_name='They do not have tools for testing')
    coughing_relative = Field(attribute='coughing_relative',
                                       column_name='I am not the one coughing it was my relative/Friend')
    travelled = Field(attribute='travelled',
                                     column_name='I travelled')
    therapy = Field(attribute='therapy',
                                         column_name='On a therapy')
    no_money = Field(attribute='no_money', column_name='No money for card/Transport')
    person_died = Field(attribute='person_died',
                                         column_name='The person died')
    afraid_stress = Field(attribute='afraid_stress', column_name='Afraid of Stress/Not Strong/crowd at the health facility')
    class Meta:
        model = ReasonNotTested
        exclude = ('is_active','modified_at','created_by','created_at','modified_by', )