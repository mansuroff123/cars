from django.db import models

# Create your models here.


class Car(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50)
    description = models.TextField()


    def __str__(self):
        return self.title
    