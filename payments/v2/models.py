from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User

class Service(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    description=models.TextField()
    logo=models.ImageField()

class Payment_users(models.Model):
    id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='usuarios')
    service_id=models.ForeignKey(Service,on_delete=models.CASCADE,related_name='services')
    Amount=models.FloatField()
    Payment_date=models.DateField()
    Expiration_date=models.DateField()

class Expired_payments(models.Model):
    Id=models.AutoField(primary_key=True)
    Payment_user_id=models.ForeignKey(Payment_users,on_delete=models.CASCADE,related_name='pagosusuarios')
    Penalty_fee_amount=models.FloatField()