from email.policy import default
from django.db import models

# Create your models here.
class book(models.Model):
    book_id = models.AutoField
    book_name = models.CharField(max_length=50)
    pubDate = models.DateField()
    genre = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to='aubook/images', default="")

    def __str__(self):
        return self.book_name