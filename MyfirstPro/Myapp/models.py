from django.db import models

# Create your models More.
class Student(models.Model):
    name=models.CharField(max_length=120)
    address=models.CharField(max_length=120)
    total=models.IntegerField()

    def __str__(self):
        return self.name