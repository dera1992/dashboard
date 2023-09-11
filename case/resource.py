from import_export import resources
from import_export.fields import Field
from .models import CaseCategory, CaseStatus


class CaseCategoryResource(resources.ModelResource):
     id = Field(attribute='id', column_name='Id')
     inquiry_for_information = Field(attribute='inquiry_for_information', column_name='Inquiry for Information')
     inquiry_for_service = Field(attribute='inquiry_for_service', column_name='Inquiry for Service')
     hoax_call = Field(attribute='hoax_call', column_name='Hoax Call')
     non_tb_calls = Field(attribute='non_tb_calls', column_name='Non-TB Calls')
     appreciation_acknowledgement = Field(attribute='appreciation_acknowledgement', column_name='Appreciation/Acknowledgement')
     service_complaint = Field(attribute='service_complaint', column_name='Service Complaint')
     technical_complaint = Field(attribute='technical_complaint', column_name='Technical Complaint')
     covid_19 = Field(attribute='covid_19', column_name='Covid-19')
     suggestions = Field(attribute='suggestions', column_name='Suggestions')
     dropped_calls = Field(attribute='dropped_calls', column_name='Dropped Calls')
     test_calls = Field(attribute='test_calls ', column_name='Test Calls')
     class Meta:
         model = CaseCategory
         fields = ('id', 'inquiry_for_information', 'inquiry_for_service', 'hoax_call','non_tb_calls','appreciation_acknowledgement',
                   'service_complaint','technical_complaint','covid_19','suggestions','dropped_calls','test_calls')


class CaseStatusResource(resources.ModelResource):
    id = Field(attribute='id', column_name='Id')
    open = Field(attribute='open', column_name='Open')
    escalated = Field(attribute='escalated', column_name='Escalated')
    pending = Field(attribute='pending', column_name='Pending')
    resolved = Field(attribute='resolved', column_name='Resolved')
    resolved_closed = Field(attribute='resolved_closed', column_name='Resolved Closed')
    class Meta:
        model = CaseStatus
        fields = ('id', 'open', 'escalated', 'pending','resolved','resolved_closed')