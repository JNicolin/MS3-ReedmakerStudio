from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
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
    
class Event(models.Model):
    gig_title = models.CharField(max_length=100, default='add a title')
    gig_description = models.TextField(blank=True)
    gig_date = models.DateField(null=True, blank=True)
    gig_location = models.CharField(max_length=100, blank=True)
    reed = models.ForeignKey(Reed, on_delete=models.SET_NULL, null=True, blank=True,related_name="targeted_gigs")

    def __str__(self):
        return f"{self.gig_title}, {self.gig_location}"

class Repertoire(models.Model):
    music_title = models.CharField(max_length=100, default='add a title')
    music_composer = models.CharField(null=True)
    music_genre = models.CharField(null=True)
    reed = models.ForeignKey(Reed, on_delete=models.SET_NULL, null=True, blank=True, related_name="repertoire_list")

    def __str__(self):
        return f"{self.music_title}, {self.music_composer}"
