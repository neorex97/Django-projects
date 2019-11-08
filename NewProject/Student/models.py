from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=120)
    address=models.CharField(max_length=120)
    phone=models.CharField(max_length=120)
    course=models.CharField(max_length=120)

    def __str__(self):
        return self.name