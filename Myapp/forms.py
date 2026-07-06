from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Userservicerequest


#import models here

class Customregisterform(UserCreationForm):
    
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    
    class Meta:
        model = CustomUser
        fields= ['username','first_name','last_name','email','phone_number','role','password1','password2']
    
class servicerequest_form(forms.ModelForm):
    
    class Meta:
        model = Userservicerequest
        fields = "__all__"
        exclude = ['status','assigned_worker']
        



    
    