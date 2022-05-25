from django.db import models
from django.contrib.auth.models import User

User._meta.get_field("email")._unique = True
User._meta.get_field("username")._unique = True

class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birthday = models.DateField()
    rewardspoints = models.IntegerField()

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderdate = models.DateField()
    ordertotal = models.DecimalField()
    isDeliver = models.BooleanField()
    isCash = models.BooleanField()
    itemsordered = models.JSONField()