from django.shortcuts import render, redirect 

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 

# Create your views here.
from django.http import HttpResponse
from .models import Cat, Toy

from .forms import FeedingForm	



# Other view functions above

class ToyList(ListView):
    model = Toy

class ToyDetail(DetailView):
    model = Toy

class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

# <model_name>_form.html

# path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add-feeding'),
# cat_id comes from the param name in the urls.py ^^^^^
def add_feeding(request, cat_id):
	# create an instance of our form, essentially filling out the form, 
	# using the data from the POST request from the cleint (think req.body, request.POST)
	form = FeedingForm(request.POST)
	# validate the form
	if form.is_valid():
		## we still need to add the cats'id to the feeding!
		# create an object to be saved be saved to the db
		new_feeding = form.save(commit=False)
		# add the cat_id to the object that is going to added as a new row in the feeding table
		# in psql
		new_feeding.cat_id = cat_id
		new_feeding.save() # enter a new row in the feeding table in psql
	return redirect('cat-detail', cat_id=cat_id)
	# cat_id is the param name on the url for cat-detail
	# the value is the param in the argument in the add_feeding function



class CatUpdate(UpdateView):
	model = Cat
	# disallow the updating of the cats name
	fields = ['breed', 'description', 'age']
	# this is how to define a redirect 
	# but we are using the get_absolute_url on the model
	# success_url = '/cats/'	


class CatDelete(DeleteView):
	model = Cat
	success_url = '/cats/'


class CatCreate(CreateView):
	model = Cat
	fields = '__all__' # referencing the model fields
	# this is how to define a redirect 
	# but we are using the get_absolute_url on the model
	# success_url = '/cats/'

# View functions are like controller functions
# they process http requests

# ============================================
#### Friday July 19th Only Code For simplicity 
#### Since we don't have models yet!
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
def home(request):

	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def cat_index(request):
	# 'cats' would be the variable name (cat) in the cats/index.html
	cats = Cat.objects.all() # Using our model to select all the rows in the cats table
	return render(request, 'cats/index.html', {'cats': cats})

# cat_id comes from the param name in the urls.py, for example
# path('cats/<int:cat_id>/'. views.cat_detail, name='cat-detail'),
def cat_detail(request, cat_id):
	# use our model to find a cat in the row that matches the cat_id
	cat = Cat.objects.get(id=cat_id)
	feeding_form = FeedingForm() # this creates a form from our class
	return render(request, 'cats/detail.html', {'cat': cat, 'feeding_form': feeding_form})