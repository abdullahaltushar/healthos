from django.db import models

# Create your models here.

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    website = models.URLField(blank=True)
    password=models.CharField(max_length=12)
    active = models.BooleanField(default=False)
    username=models.CharField(max_length=20)

    def __str__(self):
        return self.name