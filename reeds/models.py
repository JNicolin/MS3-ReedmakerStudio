from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment
from .choices import Sound, Resistance, Response, Rating, Visibility, Instrument

# Create your models here.

class Reed(models.Model):
    item_id = models.CharField(default="nn")
    item_visibility = models.IntegerField(choices=Visibility.choices, default=Visibility.PRIVATE)
    item_comment = models.CharField(max_length=200, blank=True)
    item_type = models.CharField(max_length=4, choices=Instrument.choices, default=Instrument.OBOE)
    item_creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reed_maker")
    item_rating = models.IntegerField(choices=Rating, default=Rating.PRACTICE)
    descr_resistance = models.IntegerField(choices=Resistance.choices, default=Resistance.MEDIUM)
    descr_sound = models.IntegerField(choices=Sound.choices, default=Sound.ROUND)
    descr_response = models.IntegerField(choices=Response.choices, default=Response.ACCURATE)
    descr_length = models.FloatField(null=True, blank=True)
    staple_model = models.CharField(max_length=50, blank=True)
    staple_length = models.FloatField(null=True, blank=True)
    staple_material = models.CharField(max_length=50, blank=True)
    cane_gauge_thickness = models.FloatField(null=True, blank=True)
    cane_shaper_form = models.CharField(null=True, blank=True)
    cane_supplier = models.CharField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    comments = GenericRelation(Comment)

    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.item_id}, {self.item_type}, {self.item_rating}"
    
    def get_content_type_id(self):
        return ContentType.objects.get_for_model(self.__class__).id
    
    

