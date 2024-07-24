from django.contrib import admin

# Register your models here.
from .models import Cat, Feeding,Toy

admin.site.register(Cat)  # creates a crud app for this model for our admins
admin.site.register(Feeding)
admin.site.register(Toy)