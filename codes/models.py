from django.db import models

# Create your models here.
class Code(models.Model):
    number=models.CharField(max_length=5)
    user=models.CharField(max_length=12)
    phone=models.CharField(max_length=11)

    def __str__(self):
        return str(self.user)