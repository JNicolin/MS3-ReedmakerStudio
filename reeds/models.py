from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment
from .choices import Sound, Resistance, Response, Instrument, Visibility

# Create your models here.

class Reed(models.Model):
    title = models.CharField(max_length=50)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reed_maker")
    description = models.TextField(null=True)
    photo = CloudinaryField('image', null=True, blank=True)
    instrument = models.CharField(max_length=4, choices=Instrument.choices, default=Instrument.OBOE)
    character_resistance = models.IntegerField(choices=Resistance.choices, default=Resistance.MEDIUM)
    character_sound = models.IntegerField(choices=Sound.choices, default=Sound.ROUND)
    chararacter_response = models.IntegerField(choices=Response.choices, default=Response.ACCURATE)
    staple_model = models.TextField(max_length=100, blank=True)
    staple_length = models.FloatField(null=True, blank=True)
    overall_length = models.FloatField(null=True, blank=True)
    gauge_thickness = models.FloatField(null=True, blank=True)
    cane_shaper_form = models.TextField(null=True, blank=True)
    cane_supplier = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    visibility = models.IntegerField(choices=Visibility.choices, default=Visibility.PRIVATE)

    comments = GenericRelation(Comment)

    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.title}, by: {self.creator}"
    
class Event(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100)
    reed = models.ForeignKey(Reed, on_delete=models.CASCADE, related_name="performances")

    def __str__(self):
        return f"{self.title}: {self.location}"


class Repertoire(models.Model):
    title = models.CharField(max_length=200)
    composer = models.TextField(null=True)
    genre = models.TextField(null=True)
    reed = models.ForeignKey(Reed, on_delete=models.CASCADE, related_name="repertoire_list")

    def __str__(self):
        return f"{self.title}"
