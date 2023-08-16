from django.db import models
from cabin.models import Property
from user.models import UserInfo
class PropertyReview(models.Model):
    class rating(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
    property=models.ForeignKey(Property,on_delete=models.CASCADE,related_name='propertyReview')
    review=models.TextField()
    rating=models.PositiveSmallIntegerField(choices=rating.choices,default=rating.FIVE)
    user=models.ForeignKey(UserInfo,on_delete=models.CASCADE,related_name='propertyReview')
    def __str__(self):
        return self.property.name+self.review
