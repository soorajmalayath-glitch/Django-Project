from django.contrib import admin
from .models import Userservicerequest


# Register your models here.
class MasterAdmin(admin.ModelAdmin):
    exclude = ['created_user']
    def save_model(self,request,obj,form,change):
        obj.created_user = request.user
        return super().save_model(request,obj,form,change)
    
    
class ServiceRequestadmin(MasterAdmin):
    list_display = ['customer_name','issue','location','created_at']
    

admin.site.register(Userservicerequest,ServiceRequestadmin)