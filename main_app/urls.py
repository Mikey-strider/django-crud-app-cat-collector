
from django.urls import path

from . import views # import all the functions in the views file and
# attach them to the object views

urlpatterns = [
	# django we use trailing /'s 
	# root route will just be an empty string
	# localhost:8000
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	# localhost:8000/cats
	path('cats/', views.cat_index, name='cat-index'),
	path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
	# route is used to create a cat
	path('cats/create/', views.CatCreate.as_view(), name='cat-create'),
	# class based views expect params to be name pk (primary key) 
	path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat-update'),
	path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat-delete'),
	path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add-feeding'),
	path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
	path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
	path('toys/', views.ToyList.as_view(), name='toy-index'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),

]