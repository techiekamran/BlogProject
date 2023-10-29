from django.contrib import admin
from bookapp.models import Book, Author, Address,Country
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    #readonly_fields = ('slug',)
    prepopulated_fields = {'slug':('book_title',)}
    list_filter = ('rating','author',)
    list_display = ('book_title','author',)

class AuthorAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name',)

admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Address)
admin.site.register(Country)