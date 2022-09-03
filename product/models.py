from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    def __str__(self):
        return self.title
    

    # adding an in