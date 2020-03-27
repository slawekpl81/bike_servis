from django.db import models
import datetime


# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=100)
    other = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'

class ServisClient(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12, blank=True, unique=True)
    email = models.EmailField(blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    other = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name} - {self.phone}'

    def post_name(self):
        return f'{self.name}'

class Bike(models.Model):
    mark = models.CharField(max_length=100)
    model = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(ServisClient, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, blank=True)
    year_made = models.CharField(max_length=20, blank=True)
    other = models.TextField(blank=True)

    def __str__(self):
        return f'{self.owner.post_name()} - {self.mark} {self.model}'

class Servis(models.Model):
    date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today() + datetime.timedelta(days=5))
    status = models.BooleanField(default=False)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    servis_range = models.TextField(blank=True)
    other = models.TextField(blank=True)
    def __str__(self):
        return f'{self.bike.owner}-{self.bike.mark} {self.bike.model}'



class Comments(models.Model):
    message = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now)
    author = models.CharField(max_length=50, blank=True)
    answer = models.TextField(blank=True)

    def __repr__(self):
        return f'Komentarz z dnia: {self.date}:\n {self.message}'
    def __str__(self):
        return f'Komentarz z dnia: {self.date}:\n {self.message}'




