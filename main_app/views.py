from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.http import HttpResponse
from .models import Cat, Toy

from .forms import FeedingForm


# Other view functions above

# <app_name>/_<model_name>_list.html
# main_app/toy_list.html


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('cat-index')
    else:
        error_message = "Invalid signup - try again"
  form = UserCreationForm()
  return render(request, 'signup.html', {'error_message': error_message, 'form': form})

class Home(LoginView):
  template_name = 'home.html'

# def home(request):

#     return render(request, 'home.html')


@login_required
def associate_toy(request, cat_id, toy_id):
  cat = Cat.objects.get(id=cat_id)
  cat.toys.add(toy_id)  # this adds the new row to our through table

  # Cat.objects.get(id=cat_id).toys.add(toy_id)

  return redirect('cat-detail', cat_id=cat_id)

@login_required
def remove_toy(request, cat_id, toy_id):

  cat = Cat.objects.get(id=cat_id)

  cat.toys.remove(toy_id)

  return redirect('cat-detail', cat_id=cat_id)

class ToyList(LoginRequiredMixin, ListView):
  model = Toy


# main_app/toy_detail.html
class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

# <model_name>_form.html

# path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add-feeding'),
# cat_id comes from the param name in the urls.py ^^^^^
@login_required
def add_feeding(request, cat_id):
  # create an instance of our form, essentially filling out the form,
  # using the data from the POST request from the cleint (think req.body, request.POST)
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # we still need to add the cats'id to the feeding!
    # create an object to be saved be saved to the db
    new_feeding = form.save(commit=False)
    # add the cat_id to the object that is going to added as a new row in the feeding table
    # in psql
    new_feeding.cat_id = cat_id
    new_feeding.save()  # enter a new row in the feeding table in psql
  return redirect('cat-detail', cat_id=cat_id)
  # cat_id is the param name on the url for cat-detail
  # the value is the param in the argument in the add_feeding function

class CatUpdate(LoginRequiredMixin, UpdateView):
  model = Cat
  # disallow the updating of the cats name
  fields = ['breed', 'description', 'age']
  # this is how to define a redirect
  # but we are using the get_absolute_url on the model
  # success_url = '/cats/'

class CatDelete(LoginRequiredMixin, DeleteView):
  model = Cat
  success_url = '/cats/'

class CatCreate(LoginRequiredMixin, CreateView):
  model = Cat
  # referencing the model fields
  fields = ['name', 'breed', 'description', 'age']
  # this is how to define a redirect
  # but we are using the get_absolute_url on the model
  # success_url = '/cats/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


# View functions are like controller functions
# they process http requests

# ============================================
# Friday July 19th Only Code For simplicity
# Since we don't have models yet!
# This class is simulates objects that we would retrieve from the database
# using our model!

# class Cat:
# 	def __init__(self, name, breed, description, age):
# 		self.name = name
# 		self.breed = breed
# 		self.description = description
# 		self.age = age

# cats = [
# 	Cat("Dobbie", "Sphinx", "Loves treats", 3),
# 	Cat("bear", "Sphinx", "Loves fighting", 9),
# 	Cat("taco", "Sphinx", "Loves lindsey", 3),
# 	Cat("smudge", "tiger", "Loves luna", 0),
# ]

# ============================================
# ============================================
# ============================================




@login_required
def about(request):
  return render(request, 'about.html')

@login_required
def cat_index(request):
  # 'cats' would be the variable name (cat) in the cats/index.html
  cats = Cat.objects.filter(user=request.user)  # Using our model to select all the rows in the cats table
  return render(request, 'cats/index.html', {'cats': cats})

# cat_id comes from the param name in the urls.py, for example
# path('cats/<int:cat_id>/'. views.cat_detail, name='cat-detail'),

@login_required
def cat_detail(request, cat_id):
  # use our model to find a cat in the row that matches the cat_id
  cat = Cat.objects.get(id=cat_id)

  # we want list of all the toys that cat doesn't have!
  # exclude, id__in, field look ups in django
  toys = Toy.objects.exclude(id__in=cat.toys.all().values_list('id'))
  feeding_form = FeedingForm()  # this creates a form from our class
  return render(request, 'cats/detail.html', {'cat': cat, 'feeding_form': feeding_form, 'toys': toys})