from django.db.models import Q

from .serializers import PropertySerializer
from db_models.models import Property
from django.core.exceptions import ValidationError


class PropertyService:

    def __init__(self):
        pass

    # Get All Property Service
    def get_all_property_service(self):
        # Get active property data from database using model
        # property_objects = Property.objects.filter(status__status='Active')

        # Serialize the property
        property_serializer = PropertySerializer(many=True)
        all_property = property_serializer.data
        return all_property