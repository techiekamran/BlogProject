from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify # for url contruct based on patter i.e title-1


# Create your models here.

#for many to many relationship with books model
class Country(models.Model):
    name = models.CharField(max_length=15)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "Countries List"

class Address(models.Model):
    street = models.CharField(max_length=15)
    pincode = models.IntegerField()
    city = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.street} {self.pincode} {self.city}"
    
    class Meta:
        verbose_name_plural = "Address Entries"

#many to one relationship with author feild class
# one to one relationship with address class
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address,on_delete=models.CASCADE,null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()

class Book(models.Model):
    book_title = models.CharField(max_length=30)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    #author = models.CharField(null=True,max_length=50)
    #many to one relationship with Author class
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True,related_name='books')
    is_bestselling = models.BooleanField(default=False)
    #to use slug replace id keyword with slug keyword
    slug = models.SlugField(default="",null=False)
    published_countries = models.ManyToManyField(Country,null=False)

    #does't required save fun when we use prepopulated_fields on django admin file
    def save(self,*args, **kwargs):
        self.slug = slugify(self.book_title)
        super().save(*args,**kwargs)

    #to contruct url (book-details-page,) it can be use incluse of html url tag
    def get_absolute_url(self):
        return reverse("book_details", args=[self.slug]) #replace id with slug
    

    def __str__(self):
        return f"{self.book_title} {self.rating}"