from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from scrapy_djangoitem import DjangoItem
# Create your models here.


class Cellar(models.Model):

    #True is the cellar is configure
    isConfigured = models.BooleanField(default=False)


    name = models.CharField(max_length=30)
    #location = models.CharField(max_length=30)
    #brand = models.CharField(max_length=30)
    #temperature = models.FloatField()
    #capacity = models.IntegerField()
    #humidity = models.FloatField()

    def __unicode__(self):
        return self.name


class GrapeVariety(models.Model):

    #name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):

    name = models.CharField(max_length=30)
    quantity = models.FloatField()


class Recipe(models.Model):

    RECIPE_CATEGORY = (
        ('0', 'BEEF'),
        ('1', 'BREAKFAST'),
        ('2', 'CHICKEN'),
        ('3', 'DUCK'),
        ('4', 'EGGS'),
        ('5', 'FISH'),
        ('6', 'FONDUE'),
        ('7', 'GAME'),
        ('8', 'LAMB'),
        ('9', 'LEGUME'),
        ('10', 'PASTA'),
        ('11', 'PIZZA'),
        ('12', 'PORK'),
        ('13', 'QUICHES'),
        ('14', 'RICE'),
        ('15', 'RISOTTO'),
        ('16', 'SANDWICHES'),
        ('17', 'SEAFOOD'),
        ('18', 'TOFU'),
        ('19', 'TURKEY'),
        ('20', 'VEAL'),
    )

    title = models.CharField(max_length=30)
    category = models.IntegerField(choices=RECIPE_CATEGORY)
    ingredient = models.ForeignKey(Ingredient)


class Bottle(models.Model):

    name = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=20)
    classification = models.CharField(max_length = 50)
    regulatedDesignation = models.CharField(max_length=50, null=True)
    producer = models.CharField(max_length=30)
    #grapeVariety = models.ForeignKey(GrapeVariety)
    colour = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    degreeOfAlcohol = models.CharField(max_length=10, null=True)
    sugarContent = models.CharField(max_length=20)
    evaluation = models.IntegerField(null=True)
    inStock = models.BooleanField(default=False)
    cup = models.CharField(max_length=14)


class Transaction(models.Model):

    TRANSACTION_TYPE = (
        ('0', 'Ajout'),
        ('1', 'Retrait'),
        ('2', 'Recherche'),
    )

    noTransaction = models.CharField(max_length=30)
    requestTime = models.DateTimeField(default=timezone.now, blank=True)
    completedTime = models.DateTimeField()
    completed = models.BooleanField(default=False)

class Crawler(models.Model):

    cup = models.CharField(max_length=30)