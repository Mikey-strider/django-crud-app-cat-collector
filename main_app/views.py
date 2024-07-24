from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView

# Create your views here.

# View functions are like controller function
# they process http requests

from .models import Cat, Toy
from .forms import FeedingForm


# * View Functions

def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def cat_index(request):
    # 'cats' would be the variable name (cat) in the cats/index.html
    cats = Cat.objects.all()  # using model to select all the rows in the cats table
    return render(request, "cats/index.html", {"cats": cats})


# cat_id comes from the param name in urls.py
def cat_details(request, cat_id):
    # no need for async await bc python is synchronous
    cat = Cat.objects.get(id=cat_id)
    feeding_form = FeedingForm()  # creates a form from our class
    return render(
        request, "cats/details.html", {"cat": cat, "feeding_form": feeding_form}
    )


def add_feeding(request, cat_id):
    # using the data from the POST req from the client (think req.body, request.POST)
    form = FeedingForm(request.POST)
    if form.is_valid():
        # still need to add the cat_id to the feeding
        # create an object to be saved to the db
        new_feeding = form.save(commit=False)
        # add the cat_id to the obj that is going to be added as a new row in the feeding table in
        # psql
        new_feeding.cat_id = cat_id
        new_feeding.save()  # enter the new row in the feeding table in psql
    return redirect("cat-details", cat_id=cat_id)


def toy_index(request):
    toys = Toy.objects.all()
    return render(request, "main_app/toy_list.html", {"toys": toys})


# * Class Based Views

class CatCreate(CreateView):
    model = Cat
    fields = "__all__"  # referencing the model fields
    # how to define a redirect
    # * absolute url
    # success_url = '/cats/'


class CatUpdate(UpdateView):
    model = Cat
    # disallow the updating of the cat's name
    fields = ["breed", "description", "age"]


class CatDelete(DeleteView):
    model = Cat
    # since we just deleted the resource, we have to go to the index now
    # so we need to put the abs url here
    success_url = "/cats/"


class ToyCreate(CreateView):
    model = Toy
    fields = "__all__"


class ToyUpdate(UpdateView):
    model = Toy
    fields = "__all__"


class ToyDelete(DeleteView):
    model = Toy
    success_url = "/toys/"


class ToyDetail(DetailView):
    model = Toy


class ToyList(ListView):
    model = Toy