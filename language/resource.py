from import_export import resources
from import_export.fields import Field
from .models import LanguageSelection

class LanguageSelectionResource(resources.ModelResource):
    id = Field(attribute='id', column_name='Id')
    english = Field(attribute='english', column_name='English')
    pidgin = Field(attribute='pidgin', column_name='Pidgin')
    hausa = Field(attribute='hausa', column_name='Hausa')
    yoruba = Field(attribute='yoruba', column_name='Yoruba')
    igbo = Field(attribute='igbo', column_name='Igbo')

    class Meta:
        model = LanguageSelection
        exclude = ('is_active', 'modified_at', 'created_by', 'created_at', 'modified_by')

