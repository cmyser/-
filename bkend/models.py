from django.db import models

# Create your models here.
from django.db import models
from django.shortcuts import reverse
import hashlib
from django.utils.text import slugify
from time import time


class Adress(models.Model):
    adres = models.CharField(max_length=150, db_index=True)
    number_phon = models.CharField(max_length=150)
    x_re = models.FloatField(default=0)
    y_re = models.FloatField(default=0)
    start = models.CharField(max_length=150)
    stop = models.CharField(max_length=150)
    idi = models.IntegerField(default=0)


class Service(models.Model):
    ''' таблица с услугами'''
    idi = models.IntegerField(default=0)
    serviz = models.CharField(max_length=150, db_index=True)
    coment = models.CharField(max_length=150, db_index=True)
    tip = models.CharField(max_length=150, db_index=True)
    popularity = models.IntegerField(default=0)


class Price(models.Model):
    idi = models.IntegerField(default=0)
    tip = models.CharField(max_length=150, db_index=True)
    idi_price = models.IntegerField(default=0)


class Application(models.Model):
    idi = models.IntegerField(default=0)
    coment = models.CharField(max_length=150)
    marka = models.CharField(max_length=150)
    symma = models.CharField(max_length=150)
    sevises = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    size = models.CharField(max_length=150)
    adres = models.CharField(max_length=150)
    number_phon = models.CharField(max_length=150)
    date_time_start = models.DateTimeField()
    date_and_time = models.CharField(max_length=150)


class Person(models.Model):
    paword = models.CharField(max_length=150, db_index=True)
