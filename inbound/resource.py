from import_export import resources
from import_export.fields import Field
from .models import InboundStatistics,ActualUniqueCallers, PercentageInboundCalls, CallsAbandonedIvr

class InboundStatisticsResource(resources.ModelResource):
    id = Field(attribute='id', column_name='Id')
    total_overall_calls = Field(attribute='total_overall_calls', column_name='Total overall calls')
    calls_dropped_without = Field(attribute='calls_dropped_without', column_name='Calls dropped without opting for service')
    total_serviced_calls = Field(attribute='total_serviced_calls', column_name='Total Serviced calls')
    calls_self_service = Field(attribute='calls_self_service', column_name='Calls opted for self service')
    calls_opted_agent = Field(attribute='calls_opted_agent', column_name='Calls opted for agent')
    calls_received_agent = Field(attribute='calls_received_agent', column_name='Calls received by agent')
    calls_opted_received = Field(attribute='calls_opted_received',
                                       column_name='Calls opted for agent but not received')
    agent_received_serviced = Field(attribute='agent_received_serviced', column_name='Calls opted for agent but not received and not yet serviced')
    received_been_serviced = Field(attribute='received_been_serviced', column_name='Calls opted for agent and not received but have been serviced')
    dropped_not_called_back = Field(attribute='dropped_not_called_back',
                               column_name='Dropped after connecting to agent and has not been called back')
    dropped_called_back = Field(attribute='dropped_called_back', column_name='Dropped after connecting to agent and has been called back')
    called_previous_month = Field(attribute='called_previous_month',
                                  column_name='Called Back and serviced (previous month)')
    called_review_month = Field(attribute='called_review_month', column_name='Called Back and serviced (month in review)')
    called_back_service = Field(attribute='called_back_service', column_name='Called back and serviced')
    concluded_calls = Field(attribute='concluded_calls', column_name='Concluded calls to agent')
    total_referred_testing = Field(attribute='total_referred_testing', column_name='Total callers referred for testing')

    class Meta:
        model = InboundStatistics
        exclude = ('is_active', 'modified_at', 'created_by', 'created_at', 'modified_by')

class ActualUniqueCallersResource(resources.ModelResource):
    id = Field(attribute='id', column_name='Id')
    total_overall_calls__actual_callers = Field(attribute='total_overall_calls__actual_callers',
                                                column_name='Total overall calls(Actual Callers)')
    total_overall_calls__unique_callers = Field(attribute='total_overall_calls__unique_callers',
                                                column_name='Total overall calls(Unique Callers)')
    total_serviced_calls__actual_callers = Field(attribute='total_serviced_calls__actual_callers',
                                                 column_name='Total Serviced Calls(Actual Callers)')
    total_serviced_calls__unique_callers = Field(attribute='total_serviced_calls__unique_callers',
                                                 column_name='Total Serviced Calls(Unique Callers)')
    calls_self_service__actual_callers = Field(attribute='calls_self_service__actual_callers',
                                               column_name='Calls Self Service(Actual Callers)')
    calls_self_service__unique_callers = Field(attribute='calls_self_service__unique_callers',
                                               column_name='Calls Self Service(Unique Callers)')
    calls_opted_agent__actual_callers = Field(attribute='calls_opted_agent__actual_callers',
                                              column_name='Calls Opted Agent(Actual Callers)')
    calls_opted_agent__unique_callers = Field(attribute='calls_opted_agent__unique_callers',
                                              column_name='Calls Opted Agent(Unique Callers)')
    calls_received_agent__actual_callers  = Field(attribute='calls_received_agent__actual_callers ',
                                                  column_name='Calls received by agent(Actual Callers)')
    calls_received_agent__unique_callers = Field(attribute='calls_received_agent__unique_callers ',
                                                 column_name='Calls received by agent(Unique Callers)')
    calls_opted_received__actual_callers = Field(attribute='calls_opted_received__actual_callers',
                                                 column_name='Calls Opted Received(Actual Callers)')
    calls_opted_received__unique_callers = Field(attribute='calls_opted_received__unique_callers',
                                                 column_name='Calls Opted Received(Unique Callers)')
    called_back_service__actual_callers = Field(attribute='called_back_service__actual_callers',
                                                column_name='Called Back Service(Actual Callers)')
    called_back_service__unique_callers = Field(attribute='called_back_service__unique_callers',
                                                column_name='Called Back Service(Unique Callers)')

    class Meta:
        model = ActualUniqueCallers
        exclude = ('is_active', 'modified_at', 'created_by', 'created_at', 'modified_by','total_overall_calls',
                   'total_serviced_calls','calls_self_service','calls_opted_agent','calls_received_agent',
                   'calls_opted_received','called_back_service')

class PercentageInboundCallsResource(resources.ModelResource):
    id = Field(attribute='id', column_name='Id')
    eight = Field(attribute='eight', column_name='8:00-9:00')
    nine = Field(attribute='nine', column_name='9:00-10:00')
    ten = Field(attribute='ten', column_name='10:00-11:00')
    eleven = Field(attribute='eleven', column_name='11:00-12:00')
    twelve = Field(attribute='twelve', column_name='12:00-1:00')
    thirteen = Field(attribute='thirteen', column_name='1:00-2:00')
    fourteen = Field(attribute='fourteen', column_name='2:00-3.00')
    fifteen = Field(attribute='fifteen', column_name='3:00-4:00')
    sixteen = Field(attribute='sixteen', column_name='4:00-5:00')

    class Meta:
        model = PercentageInboundCalls
        exclude = ('is_active', 'modified_at', 'created_by', 'created_at', 'modified_by')

class CallsAbandonedIvrResource(resources.ModelResource):
    id = Field(attribute='id', column_name='Id')
    abandoned_ivr_within = Field(attribute='abandoned_ivr_within', column_name='Abandoned on IVR within Working Hour')
    abandoned_ivr_after = Field(attribute='abandoned_ivr_after', column_name='Abandoned on IVR After working Hour')
    abandoned_ivr_public = Field(attribute='abandoned_ivr_public', column_name='Abandoned on IVR on Public Holidays')
    abandoned_ivr_weekend = Field(attribute='abandoned_ivr_weekend', column_name='Abandoned on IVR on Weekends')

    class Meta:
        model = CallsAbandonedIvr
        exclude = ('is_active', 'modified_at', 'created_by', 'created_at', 'modified_by')