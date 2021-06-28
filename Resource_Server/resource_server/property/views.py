from oauth2_provider.contrib.rest_framework import OAuth2Authentication
from oauth2_provider.decorators import protected_resource, rw_protected_resource
from oauth2_provider.views.mixins import ProtectedResourceMixin
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .services import PropertyService
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, ValidationError


# Get All Property Endpoint
@api_view(["POST"])
@csrf_exempt
@protected_resource()
def get_all_property(request):
    # Calling Property Service
    property_service = PropertyService()

    try:
        # Getting Property Data from Service
        all_property = property_service.get_all_property_service()

        return JsonResponse({'property': all_property, 'message': 'All Properties Retrieved Successfully.'},
                            safe=False, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)