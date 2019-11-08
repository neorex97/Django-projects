from django.db import models

# Create your models More.
class Product(models.Model):
    name=models.CharField(max_length=120)
    category=models.CharField(max_length=120)
    price=models.IntegerField()
    spec=models.CharField(max_length=120)

    def __str__(self):
        return self.name