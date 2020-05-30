from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from bkend.models import *


class AdressAdmin(admin.ModelAdmin):
    """Комнаты чата"""
    list_display = ("adres", "number_phon")

    # def invited_user(self, obj):
    #     return "\n".join([user.username for user in obj.invited.all()])

class ServiceAdmin(admin.ModelAdmin):
    list_display = ("serviz", "idi")

class PriceAdmin(admin.ModelAdmin):
    list_display = ("idi", "idi_price")

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("idi", "coment")




admin.site.register(Adress, AdressAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Person)
