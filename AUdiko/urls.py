from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('about', views.about, name='About'),
    path('contact', views.contact, name='Contact'),
    path('genres', views.geners, name='Geners'),
    path('authors', views.authors, name='Authors'),
    path('mybooks', views.myBooks, name='MyBooks'),
    path('bookview/<int:myid>', views.bookView, name='BookView'),
]
