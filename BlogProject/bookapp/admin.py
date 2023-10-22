from django.contrib import admin
from bookapp.models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    #readonly_fields = ('slug',)
    prepopulated_fields = {'slug':('book_title',)}
    list_filter = ('rating','author',)
    list_display = ('book_title','author',)

admin.site.register(Book,BookAdmin)
