from django.db import models
from django.urls import reverse


# Create your models here.
# we are inheriting the necessary methods from django premade classes
class Cat(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    # absolute redirect in class
    def get_absolute_url(self):
        return reverse("cat-details", kwargs={"cat_id": self.id})


MEALS = (
    ("B", "Breakfast"),
    ("L", "Lunch"),
    ("D", "Dinner"),
)


class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(max_length=1, choices=MEALS, default=MEALS[0][0])
    # if we delete the cat, then we will delete all of the data associated with thtat specific cat
    # meaning any relational data is also deleted
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"


class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"A {self.color} {self.name}"
    
    def get_absolute_url(self):
        return reverse("toy-detail", kwargs={"pk": self.id})
    