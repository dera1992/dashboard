from import_export import resources
from import_export.fields import Field
from .models import SourceHotlineInformation



class SourceHotlineInformationResource(resources.ModelResource):
     id = Field(attribute='id', column_name='Id')
     radio = Field(attribute='radio', column_name='Radio')
     tv = Field(attribute='tv ', column_name='TV')
     friends_family = Field(attribute='friends_family', column_name='Friends/Family')
     handbill_posters= Field(attribute='handbill_posters', column_name='Handbill/Posters')
     sms = Field(attribute='sms', column_name='SMS')
     training_and_campaign = Field(attribute='training_and_campaign', column_name='Training and campaign')
     facebook_twitter_instagram = Field(attribute='facebook_twitter_instagram',
                                   column_name='Facebook/Twitter/Instagram')
     schools = Field(attribute='schools',column_name='Schools')
     ppmvs = Field(attribute='ppmvs',column_name='Ppmvs')
     religious_settings = Field(attribute='religious_settings',
                                      column_name='Religious Settings')

     class Meta:
         model = SourceHotlineInformation
         exclude = ('is_active','modified_at','created_by','created_at','modified_by' )
