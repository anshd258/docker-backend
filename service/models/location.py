from django.db import models
from django.db.models import F


class Location(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(max_length=255)
    address = models.TextField(max_length=255)
    max_persons = models.IntegerField(default=0)
    location_type = models.TextField()
    base_surge = models.FloatField(default=1.0)
    surge = models.FloatField(default=1.0)
    occupancy = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name) + " (" + str(self.surge) + "x )"

    def save(self, **kwargs):
        self.calculate_surge()
        super().save(**kwargs)

    def calculate_surge(self):
        try:
            self.surge = (self.occupancy / self.max_persons) + self.base_surge
        except Exception as e:
            self.surge = self.base_surge

    def check_in(self, no_of_persons):
        self.occupancy = F('occupancy') + no_of_persons
        self.save()

    def check_out(self, no_of_persons):
        self.occupancy = 0 if self.occupancy < no_of_persons else F('occupancy') - no_of_persons
        self.save()
