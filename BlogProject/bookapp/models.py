from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify # for url contruct based on patter i.e title-1


# Create your models here.
class Book(models.Model):
    book_title = models.CharField(max_length=30)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    author = models.CharField(null=True,max_length=50)
    is_bestselling = models.BooleanField(default=False)
    #to use slug replace id keyword with slug keyword
    slug = models.SlugField(default="",null=False)

    #does't required save fun when we use prepopulated_fields on django admin file
    def save(self,*args, **kwargs):
        self.slug = slugify(self.book_title)
        super().save(*args,**kwargs)

    #to contruct url (book-details-page,) it can be use incluse of html url tag
    def get_absolute_url(self):
        return reverse("book_details", args=[self.slug]) #replace id with slug
    

    def __str__(self):
        return f"{self.book_title} {self.rating}"