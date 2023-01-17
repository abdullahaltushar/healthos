from django.db import models
from Company.models import Company
from Plan.models import Plan

from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=14)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    primary_number = models.BooleanField(default=True)
    active = models.BooleanField(default=False)


