from django.db import models

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    contract_length = models.PositiveIntegerField()

    def __str__(self):
        return self.name
