from import_export import resources
from import_export.fields import Field
from .models import GeographicalDistribution, GenderGeographical


class GeographicalDistributionResource(resources.ModelResource):
     id = Field(attribute='id', column_name='Id')
     north_west = Field(attribute='north_west', column_name='North-Wast')
     north_east = Field(attribute='north_east', column_name='North-East')
     north_central = Field(attribute='north_central', column_name='North-Central')
     south_south = Field(attribute='south_south', column_name='South-South')
     south_east = Field(attribute='south_east', column_name='South-East')
     south_west = Field(attribute='south_west', column_name='South-West')
     class Meta:
         model = GeographicalDistribution
         fields = ('id', 'north_west', 'north_east', 'north_central','south_south','south_east',
                   'south_west ')


class GenderGeographicalResource(resources.ModelResource):
    id = Field(attribute='id', column_name='Id')
    north_west__male = Field(attribute='north_west__male', column_name='North-Wast Male')
    north_west__female = Field(attribute='north_west__female', column_name='North-Wast Female')
    north_east__male = Field(attribute='north_east__male', column_name='North-East Male')
    north_east__female = Field(attribute='north_east__female', column_name='North-East Female')
    north_central__male = Field(attribute='north_central__male', column_name='North-Central Male')
    north_central__female = Field(attribute='north_central__female', column_name='North-Central Female')
    south_south__male = Field(attribute='south_south__male', column_name='South-South Male')
    south_south__female = Field(attribute='south_south__female', column_name='South-South Female')
    south_east__male = Field(attribute='south_east__male', column_name='South-East Male')
    south_east__female = Field(attribute='south_east__female', column_name='South-East Female')
    south_west__male = Field(attribute='south_west__male', column_name='South-West Male')
    south_west__female = Field(attribute='south_west__female', column_name='South-West Female')
    class Meta:
        model = GenderGeographical
        fields = ('id', 'north_west__male','north_west__female', 'north_east__male','north_east__female',
                  'north_central__male','north_central__female', 'south_south__male','south_south__male',
                  'south_east__male','south_east__female','south_west__male','south_west__female')