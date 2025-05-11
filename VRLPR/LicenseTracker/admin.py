from django.contrib import admin
from . models import Person, License, Car, Junktion
admin.site.register(Person)
admin.site.register(Car)
admin.site.register(License)
admin.site.register(Junktion)