from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login_page/', views.login_view, name='login_page'),
    path('user_page/',views.user_page,name='success'),
    path('signup/',views.signup_view,name='signup'),
    path('logout_page/',views.logout_page,name='logout'),
    path('servicerequest/',views.ServiceRequest,name='services'),
    path('customerserviceview/',views.customerserviceview,name='service_request'),
    path('worker_dashboard/',views.worker_dashboard,name='workerserviceview'),
    path('update_dashboard/<int:id>/',views.update_dashboard,name='update_dashboard')
    
]