from rest_framework import serializers
from django.contrib.auth.models import User

from bkend.models import *


class AdressSerializers(serializers.ModelSerializer):
    """Сериализация adresa """
    adres = serializers.CharField(max_length=150)
    number_phon = serializers.CharField(max_length=150)
    x_re = serializers.FloatField(default=0)
    y_re = serializers.FloatField(default=0)
    start = serializers.CharField(max_length=150)
    stop = serializers.CharField(max_length=150)
    idi = serializers.IntegerField(default=0)

    class Meta:
        model = Adress
        fields = ("adres", "number_phon", "x_re", "y_re", "start", "stop", "idi")


class ServiseSerializers(serializers.ModelSerializer):
    idi = serializers.IntegerField(default=0)
    serviz = serializers.CharField(max_length=150)
    coment = serializers.CharField(max_length=150)
    tip = serializers.CharField(max_length=150)
    popularity = serializers.IntegerField(default=0)

    class Meta:
        model = Service
        fields = ("idi", "serviz", "coment", "tip", "popularity")


class PriceSerializers(serializers.ModelSerializer):
    idi = serializers.IntegerField(default=0)
    tip = serializers.CharField(max_length=150)
    idi_price = serializers.IntegerField(default=0)

    class Meta:
        model = Price
        fields = ("idi", "tip", "idi_price")

class ApplicationSerializers(serializers.ModelSerializer):
    idi = serializers.IntegerField(default=0)
    coment = serializers.CharField(max_length=150)
    marka = models.CharField(max_length=150)
    symma = serializers.CharField(max_length=150)
    sevises = serializers.CharField(max_length=150)
    phone = serializers.CharField(max_length=150)
    size = serializers.CharField(max_length=150)
    adres = serializers.CharField(max_length=150)
    number_phon = serializers.CharField(max_length=150)
    date_time_start = serializers.DateTimeField()
    date_and_time = serializers.CharField(max_length=150)

    class Meta:
        model = Application
        fields = ("idi", "coment", "marka", "symma", "sevises", "phone", "size", "adres", "number_phon", "date_time_start", "date_and_time")

class PersonSerializers(serializers.ModelSerializer):
    paword = serializers.CharField(max_length=150)
    class Meta:
        model = Person
        fields = ("paword",)
