from django.db import models

class Visibility(models.IntegerChoices):
    PRIVATE = 0, "Private"
    PUBLIC = 1, "Public"
    
class Resistance(models.IntegerChoices):
    SOFT = 0, "Soft"
    MEDIUM = 1, "Medium"
    HARD = 2, "Hard"

class Sound(models.IntegerChoices):
    SHRILL = 0, "Shrill"
    BRIGHT = 1, "Bright"
    ROUND = 2, "Round"
    DARK = 3, "Dark"
    DULL = 4, "Dull"

class Response(models.IntegerChoices):
    LIGHT = 0, "Light"
    ACCURATE = 1, "Accurate"
    LATE = 2, "Late"

class Rating(models.IntegerChoices):
    USELESS = 0, "Useless"
    PRACTICE = 1, "Practice"
    PERFORMANCE = 2, "Performance"
    PREMIUM = 3, "Premium"

class Instrument(models.TextChoices):
    OBOE = "ob", "Oboe"
    DAMORE = "da", "Oboe d'Amore"
    ANGLAIS = "ca", "Cor Anglais"
    BASS = "bo", "Bass Oboe"
    HECKEL = "hp", "Heckelphone"
    BASSOON = "bs", "Bassoon"
    CONTRABASSOON = "kb", "Contrabassoon"
    BBC = "BbC", "Bb Clarinet"
    AC = "AC", "A Clarinet"
    CC = "CC", "C Clarinet"
    EBC = "EbC", "Eb Clarinet"
    BC = "BC", "Bass Clarinet"
    KC = "KC", "Contrabass Clarinet"
    SS = "SS", "Soprano Saxophone"
    AS = "AS", "Alto Saxophone"
    TS = "TS", "Tenor Saxophone"
    BS = "BS", "Bass Saxophone"
    KS = "KS", "Contrabass Saxophone"