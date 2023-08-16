from django.db import models
from cabin.models import Property
class PropertyMetaData(models.Model):
    property=models.ForeignKey(Property,on_delete=models.CASCADE,related_name='propertyMetaData')
    key=models.TextField()
    Value=models.TextField()
    def __str__(self):
        return self.property.name+self.key