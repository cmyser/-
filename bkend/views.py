from django.shortcuts import render

# Create your views here.
from typing import Type, List

from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from django.contrib.auth.models import User

from bkend.models import *
from bkend.serializers import *


class Adresses(APIView):
    """Комнаты чата"""
    # permission_classes: List[Type[IsAuthenticated]] = [permissions.IsAuthenticated, ]

    def get(self, request):
        adds = Adress.objects.all()
        serializer = AdressSerializers(adds, many=True)
        return Response({"adds": serializer.data})

    def post(self, request):
        Adress.objects.create(adres=request.adres)
        return Response(status=201)

class Servises(APIView):
    def get(self, request):
        adds = Service.objects.all()
        serializer = ServiseSerializers(adds, many=True)
        return Response({"adds": serializer.data})

    def post(self, request):
        Service.objects.create(adres=request.adres)
        return Response(status=201)

class Prices(APIView):
    def get(self, request):
        adds = Price.objects.all()
        serializer = PriceSerializers(adds, many=True)
        return Response({"adds": serializer.data})

    def post(self, request):
        Price.objects.create(adres=request.adres)
        return Response(status=201)


class Applications(APIView):
    def get(self, request):
        adds = Application.objects.all()
        serializer = ApplicationSerializers(adds, many=True)
        return Response({"adds": serializer.data})

    def post(self, request):
        Application.objects.create(adres=request.adres)
        return Response(status=201)


class Persons(APIView):
    def get(self, request):
        adds = Person.objects.all()
        serializer = PersonSerializers(adds, many=True)
        return Response({"adds": serializer.data})

    def post(self, request):
        Person.objects.create(id=request.id)
        return Response(status=201)
