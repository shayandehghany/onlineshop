from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    # cover = models.ImageField(upload_to='products/cover', null=True, blank=True)
    # quantity = models.PositiveIntegerField(default=0)

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)