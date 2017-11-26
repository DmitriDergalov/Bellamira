from django.db import models

class Suit(models.Model):
    GENDERS = (
        ('C','Cavalier'),
        ('D','Dame'),
    )
    code = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDERS)
    style = models.CharField(max_length=20)
    sizes = models.CharField(max_length=5)
    description = models.TextField()
    sebest = models.PositiveSmallIntegerField()
    person = models.CharField(max_length=40)
    default_rent_price = models.PositiveSmallIntegerField()
    rent_price_partners = models.PositiveSmallIntegerField()
    rent_price_students = models.PositiveSmallIntegerField()
    rent_price_person = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.code
	
class Rent(models.Model):
    suit = models.ForeignKey(Suit)
    set = models.TextField()
    renter_info = models.TextField()	
    event_date = models.DateField()
    event_info = models.TextField()
    price = models.SmallIntegerField()
    giving_date = models.DateField()
    return_date = models.DateField()
    notes = models.TextField()

class Accessory(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    suits = models.ManyToManyField(Suit)

    def __unicode__(self):
        return self.name