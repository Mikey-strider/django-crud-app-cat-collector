from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.

# Add the Toy model
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toy-detail', kwargs={'pk': self.id})
class Cat(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  age = models.IntegerField()
  description = models.TextField(max_length=250)
  toys = models.ManyToManyField(Toy)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    #path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
    # cat_id is the param, so thats why we see it in kwargs
    return reverse("cat-detail", kwargs={"cat_id": self.id})

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner'),
)


class Feeding(models.Model):
  date = models.DateField('Feeding-Date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[1][0]
  )

  # create a cat_id column on the Feeding table in the database
  # (it automatically appends, _id, you don't put that. Just lowercase modelname of related model)
  cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"



