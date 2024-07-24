from django.contrib import admin

from .models import Cat, Feeding, Toy
# Register your models here.
admin.site.register(Cat) # creates a crud app for this model for our admins
admin.site.register(Feeding)
admin.site.register(Toy)