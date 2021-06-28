from django.urls import include, path
from . import views

# URL Patterns related to Property
urlpatterns = [
  path('get_all', views.get_all_property),
]