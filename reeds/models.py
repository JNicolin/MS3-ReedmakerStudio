from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment
from .choices import Sound, Resistance, Response, Instrument, Visibility

# Create your models here.
class Reed(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reed_maker")
    title = models.CharField(max_length=200,unique=True)
    description = models.TextField()
    photo = CloudinaryField('image', default='placeholder')
    instrument = models.CharField(max_length=4, choices=Instrument.choices)
    character_resistance = models.IntegerField(choices=Resistance.choices, default=Resistance.MEDIUM)
    character_sound = models.IntegerField(choices=Sound.choices, default=Sound.ROUND)
    chararacter_response = models.IntegerField(choices=Response.choices, default=Response.ACCURATE)
    staple_model = models.TextField(max_length=100)
    staple_length = models.FloatField()
    overall_length = models.FloatField()
    gauge_thickness = models.FloatField()
    cane_shaper_form = models.TextField()
    cane_supplier = models.TextField()
    #gig = models.ForeignKey(Occasion, related_name=event)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    visibility = models.IntegerField(choices=Visibility.choices, default=Visibility.PRIVATE)

    comments = GenericRelation(Comment)

    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.title}: {self.creator}"