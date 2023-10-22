from django.shortcuts import render
from bookapp.models import Book
from django.shortcuts import get_object_or_404
from django.db.models import Avg
# Create your views here.

def book_outlet(request):
    all_books = Book.objects.all().order_by('-rating') #sort using order_by
    numbers_of_books = all_books.count()
    average_rating = all_books.aggregate(Avg("rating")) #pass feild name rating__avg, rating__min
    return render(request,'bookapp/book.html',{'all_books':all_books,
                                               'numbers_of_books':numbers_of_books,
                                               'average_rating':average_rating,})

def book_details(request,slug): #replace id with slug
    #book = Book.objects.get(pk=id)
    #book = get_object_or_404(Book,pk=id)
    book = get_object_or_404(Book,slug=slug) #replace pk=id with slug
    return render(request,'bookapp/book-details.html',{
        'book_title':book.book_title,
        'book_author':book.author,
        'book_rating': book.rating,
        'is_bestselling': book.is_bestselling,
    })
