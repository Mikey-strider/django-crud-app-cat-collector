from django.contrib import admin

<<<<<<< HEAD
from .models import Cat, Feeding, Toy
# Register your models here.
admin.site.register(Cat) # creates a crud app for this model for our admins
=======
# Register your models here.
from .models import Cat, Feeding,Toy

admin.site.register(Cat)  # creates a crud app for this model for our admins
>>>>>>> 9b4e396adaec23043e4f1f29ffbb455999e9633b
admin.site.register(Feeding)
admin.site.register(Toy)