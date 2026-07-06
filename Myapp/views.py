from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser,Userservicerequest
from .forms import Customregisterform,servicerequest_form
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,'index.html')
        
def user_page(request):
    return render(request,"user_page.html")

def login_view(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            
            login(request, user)
            if user.role == 'user':
                return redirect('success')
            elif user.role == 'worker':
                
                return redirect('workerserviceview')
            
        else:
          
          messages.error(request, "Invalid username or password")
          
    return render(request, 'login.html')
    
from django.shortcuts import render, redirect
from django.contrib import messages

def signup_view(request):
    if request.method == "POST":
        form = Customregisterform(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']

            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return render(request, "signup.html", {"form": form})

            user = form.save(commit=False)
            user.role = form.cleaned_data['role']
            user.set_password(form.cleaned_data['password1'])
            user.save()

            messages.success(request, "Account created successfully")
            return redirect("login_page")

    else:
        form = Customregisterform()

    return render(request, "signup.html", {"form": form})

def logout_page(request):
    logout(request)
    messages.success(request,"logged out successfully!!!!  Login again!!!!")
    return redirect('login_page')

def ServiceRequest(request):
    if request.method == "POST":
        obj = servicerequest_form(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
            messages.success(request,"Request Submitted Successfully!!!")   
             
        return redirect('success')
        
        # return HttpResponse('Data Added')
    else:
        obj = servicerequest_form()
    return render(request,'service.html',{'x':obj})    

def customerserviceview(request):
    service = Userservicerequest.objects.all()
    return render(request,'userservice.html',{'x':service})

@login_required
def worker_dashboard(request):
    service = Userservicerequest.objects.filter(
        assigned_worker=request.user,status__in=['pending','In progress'])
    if not service.exists():
        messages.success(request,"Good Job !! No Pending request")
        return render(request,'worker_service.html')
    
    return render(request,'worker_service.html',{'x':service})

@login_required
def update_dashboard(request,id):
    ob = get_object_or_404(Userservicerequest, id=id)
    if request.method == 'POST': 
        ob.status = request.POST.get('status')
        ob.save()
    messages.success(request,"Status updated successfully")
    
    
    return redirect('workerserviceview')
    