from django.urls import path
from bookapp import views
urlpatterns = [
    path('book/',views.book_outlet,name='all_books'),
    path('book-details<slug:slug>',views.book_details,name='book_details'),
    #path('book-details<int:id>',views.book_details,name='book_details'),
]

