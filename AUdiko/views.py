from django.shortcuts import render
from django.http import HttpResponse
from .models import book
from math import ceil

# Create your views here.
def index(request):
    books = book.objects.all()
    n = len(books)
    nslides = n//4 + ceil((n/4) - (n//4))
    params = {'no_of_slides': nslides, 'range':range(1, nslides), 'book':books}
    return render(request, 'aubook/index.html', params)

def contact(request):
    return HttpResponse('Contact')

def about(request):
    return HttpResponse('About')

def geners(request):
    all_genres = []
    book_genre = book.objects.values('genre')
    list_genre = {item['genre'] for item in book_genre}
    for gen in list_genre:
        books = book.objects.filter(genre = gen)
        n = len(books)
        nslides = n//4 + ceil((n/4) - (n//4))
        all_genres.append([books, range(1, nslides), nslides])

    params = {'all_genres': all_genres}
    return render(request, 'aubook/genre.html', params)

def myBooks(request):
    return HttpResponse('My books')

def authors(request):
    return HttpResponse('Authors')

def bookView(request, myid):
    viewbook = book.objects.filter(id=myid)
    print(viewbook)
    return render(request, 'aubook/bookview.html', {'book':viewbook[0]})