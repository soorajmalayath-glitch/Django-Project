from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    
    ROLE_CHOICES = (
        ('user','User'),
        ('worker','Worker'),
    )
    
    phone_number = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES,help_text='Select category')
    
    
class Userservicerequest(models.Model):
    
    customer_name = models.CharField(max_length=100)
    
    SERVICE_CHOICES=[
        ('electrical','Electrical'),
        ('plumbing','Plumber'),
        ('furniture','Furniture'),
        ('other','other')
    ]
    
    issue = models.CharField(max_length=100,choices=SERVICE_CHOICES)
    Description = models.CharField(max_length=200,null=True,blank=True)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    STATUS_CHOICES = (
        ('pending','Pending'),
        ('in-progress','In Progress'),
        ('completed','Completed')
    )
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default='pending')
    assigned_worker = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,limit_choices_to={"role":"worker"})
    
    class Master(models.Model):
        isactive = models.BooleanField(default=True)