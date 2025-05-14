from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.contenttypes.fields import GenericRelation
from comments.models import Comment

# Create your models here.
CH_RESISTANCE = ((0, "Soft"), (1, "Medium")),((2, "Hard"))
CH_SOUND = ((0, "Shrill"), (1, "Bright")), ((2, "Round")), ((3, "Dark")), ((4, "Dull"))
CH_RESPONSE = ((0, "Light"), (1, "Accurate")),((2, "Late"))
CH_INSTRUMENT = [
    (
        "Oboe",
        ("ob", "Oboe"),
        ("da","Oboe d'Amore"),
        ("ca", "Cor Anglais"),
        ("bo", "Bass Oboe"),
        ("hp", "Heckelphone"),
    ),
    (
        "Basson",
        ("ob", "Basson"),
        ("da","Kontrabass Basson"),
    ),
    (   
        "Clarinet",
        ("BbC", "Bb Clarinet"),
        ("AC","A Clarinet"),
        ("CC", "C Clarinet"),
        ("EbC", "Eb Clarinet"),
        ("BC", "Bass Clarinet"),
        ("KC", "Kontrabass Clarinet"),
    ),
    (
        "Saxophone",
        ("SS", "Soprano Saxophone"),
        ("AS","Alto Saxophone"),
        ("TS", "Tenor Saxophone"),
        ("BS", "Bass Saxophone"),
        ("KS", "Kontrabass Saxophone"),
    )
]                                        

class Reed(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reed_maker")
    title = models.CharField(max_length=200,unique=True)
    description = models.TextField()
    photo = CloudinaryField('image', default='placeholder')
    instrument = models.CharField(max_length=2, choices=CH_INSTRUMENT)
    char_resistance = models.IntegerField(choices=CH_RESISTANCE, default=1)
    char_sound = models.IntegerField(choices=CH_SOUND, default=2)
    char_response = models.IntegerField(choices=CH_RESPONSE, default=1)
    staple_model = models.TextField(max_length=100)
    staple_length = models.FloatField()
    overall_length = models.FloatField()
    gauge_thickness = models.FloatField()
    shaper_form = models.TextField()
    cane_supplier = models.TextField()
    gig = models.ForeignKey(Occasion, related_name=event)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    comments = GenericRelation(Comment)

    Class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.title}: {self.creator}"