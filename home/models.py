from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    income = models.FloatField()
    expense = models.FloatField(null=True,blank=True)
    balance = models.FloatField(null=True)
    
    


class Expense(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    TYPE = (
        ('Positive','Positive'),
        ('Negative','Negative')
    )
    name = models.CharField( max_length=50)
    amount = models.FloatField()
    expense_type = models.CharField(max_length=50,choices = TYPE)

    def __str__(self):
        return self.name