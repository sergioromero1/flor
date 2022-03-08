from tkinter import CASCADE
from django.db import models
from users.models import User

class Flower(models.Model):

    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    unit_price = models.FloatField()

    def __str__(self):
        return self.name

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower,on_delete=models.PROTECT)
    units = models.IntegerField(default=0)
    observations_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField("date published",auto_now_add=True)

    def __str__(self):
        return 'Orden ' + str(self.pk)
