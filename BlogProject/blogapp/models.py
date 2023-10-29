from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    author_email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='posts')
    post_title = models.CharField(max_length=15)
    excerpt = models.CharField(max_length=15)
    image_name = models.CharField(max_length=15)
    Date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    slug = models.SlugField(unique=True,db_index=True)
    tag = models.ManyToManyField(Tag)

    # def __str__(self):
    #     return self.post_title