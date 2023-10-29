from django.contrib import admin
from blogapp.models import Post, Author, Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author','tag','Date',)
    list_display = ('post_title','author','Date',)
    prepopulated_fields = {'slug':('post_title',)}

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
