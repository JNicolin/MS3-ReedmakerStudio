from django.db import models
from reeds.models import Reed

# Create your models here.
class Event(models.Model):
    gig_title = models.CharField(max_length=100, default='add a title')
    gig_description = models.TextField(blank=True)
    gig_date = models.DateField(null=True, blank=True)
    gig_location = models.CharField(max_length=100, blank=True)
    reed = models.ForeignKey(Reed, on_delete=models.SET_NULL, null=True, blank=True,related_name="targeted_gigs")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.gig_title}, {self.gig_location}"
