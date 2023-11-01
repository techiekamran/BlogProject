from django.db import models


# Create your models here.

# this model will save the form data into db

class ReviewApp(models.Model):
    username = models.CharField(max_length=10)
    review_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.username

    