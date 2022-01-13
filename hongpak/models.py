from django.db import models
class Hotel(models.Model):
    Hotel_name = models.CharField(max_length=50)
    Address = models.TextField(max_length=500)
    Phone = models.CharField(max_length=10)
    Price_per_month = models.CharField(max_length=10)
    Price_per_day = models.CharField(max_length=10)
    Facilities = models.TextField(max_length=500)
    Detail = models.TextField(max_length=500)
    Place_nears = models.TextField(max_length=500)
    def __str__(self) -> str:
        return self.Hotel_name

class Room(models.Model):
    Building = models.CharField(max_length=5)
    Number = models.CharField(max_length=10)
    TYPE = (
        (0, 'Fill in'),
        (1,'Air condition room'),
        (2,'Fan '),
    )
    Type = models.IntegerField(default=0 ,choices=TYPE)
    Price = models.IntegerField(max_length=10)
    STATUS = (
        (0, 'Fill in'),
        (1, 'Vacant'),
        (2, 'Assign'),
        (3, 'Occupied'),
    )
    Status = models.IntegerField(default=0,choices=STATUS)




# Create your models here.
