from django.db import models
import datetime


# Create your models here.

class ServisClient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField(blank=True)
    mikesz = models.BooleanField(default=False)
    cash_reg = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    other = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} - {self.phone}'
    def post_name(self):
        return f'{self.name}'

class Bike(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(ServisClient, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, blank=True)
    date_made = models.DateField(blank=True)
    other = models.TextField(blank=True)

    def __str__(self):
        return f'{self.owner.post_name()} - {self.name}'
class Servis(models.Model):
    date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    servis_range = models.TextField()
    expense = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    other = models.TextField(blank=True)



class Comments(models.Model):
    message = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now)
    author = models.CharField(max_length=50, blank=True)
    answer = models.TextField(blank=True)




