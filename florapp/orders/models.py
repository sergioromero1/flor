from pyexpat import model
from django.db import models

class Order(models.Model):

    units = models.IntegerField(default=0)
    unit_price = models.FloatField()
    observations_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return 'Orden ' + str(self.pk)

class Flower(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    flower_name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    species = models.CharField(max_length=300)

    def __str__(self):
        return self.flower_name
