from django.db import models


# Create your models here.
# Property
class Property(models.Model):
    street = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 't_property'
