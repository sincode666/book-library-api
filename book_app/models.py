from django.db import models

# Create your models here.
class book_str(models.Model):
    book_title=models.CharField(max_length=200)
    book_author=models.CharField(max_length=100)
    book_price=models.FloatField()
    book_in_stock=models.BooleanField(default=True)