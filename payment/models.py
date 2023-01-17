
from datetime import datetime, timedelta
from django.db import models
from numpy import ma
from user.models import CustomUser
from Plan.models import Plan

# Create your models here.
class Payment(models.Model):
    username=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    payment=models.DateField(default=datetime.now())
    payment_amount=models.CharField(max_length=12)
    payment_number=models.CharField(max_length=11)
    payment_id=models.CharField(max_length=21)
    package=models.ForeignKey(Plan, on_delete=models.CASCADE)
    expire_date=models.DateField(default=datetime.now()+timedelta(days=30))
    expire_year=models.DateField(default=datetime.now()+timedelta(days=365))
    def __str__(self):
        return self.payment_amount


