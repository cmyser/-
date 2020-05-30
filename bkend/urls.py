from django.urls import path
from bkend.views import *

from bkend.models import *
app_name = "bkend"

urlpatterns = [
    path('adresses/', Adresses.as_view()),
    path('servises/', Servises.as_view()),
    path('prices/', Prices.as_view()),
    path('applications/', Applications.as_view()),
    path('persons/', Persons.as_view()),
]
