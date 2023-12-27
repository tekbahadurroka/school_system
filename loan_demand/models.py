from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class LoanDmand(models.Model):
    loan_no = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    old_country = models.CharField(max_length=150)
    old_district = models.CharField(max_length=100)
    old_municipilaty = models.CharField(max_length=200)
    old_word_no = models.CharField(max_length=2)
    old_village = models.CharField(max_length=200)
    zone =models.CharField(max_length=100)
    country = models.CharField(max_length=150)
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    municipilaty = models.CharField(max_length=200)
    word_no = models.CharField(max_length=2)
    village = models.CharField(max_length=200)
    greand_father = models.CharField(max_length=150)
    father_husband = models.CharField(max_length=150)
    citizenship_no = models.CharField(max_length=150)
    issue_place = models.CharField(max_length=150)
    isssue_date = models.CharField(max_length=50)
    age = models.CharField(max_length=2)
    loan_amount = models.CharField(max_length=7)
    loan_text = models.CharField(max_length=300)
    maturity_age = models.CharField(max_length=50)
    propose = models.CharField(max_length=150)
    document = models.FileField(null=True)
    status = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
