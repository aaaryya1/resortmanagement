from django import forms
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

    
class Room(models.Model):
    ROOM_CATEGORIES =(
        ('suite','suite'),
        ('deluxe','deluxe'),
        ('club suite','club suite'),
        ('Presidential Suite','Presidential Suite')
    )
    category=models.CharField(max_length=20,choices=ROOM_CATEGORIES,default='deluxe')
    room_number = models.IntegerField(unique=True)
    room_type = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    image=models.ImageField(upload_to='roomimage',default='default.jpg')
    description = models.TextField(default="Default description") 
    

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=10,blank=True)

class Booking(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    date=models.DateField(default=timezone.now)
    check_in = models.DateField()
    check_out = models.DateField()
    userinfo=models.ForeignKey(UserInfo,on_delete=models.CASCADE,null=True,blank=True)
    
    status= (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('canceled', 'Canceled'),
    )
    status = models.CharField(max_length=20, choices=status, default='pending')

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()











   

   

    
   







