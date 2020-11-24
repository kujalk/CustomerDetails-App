from django.urls import path
from CustomerInfo import views
from django.conf.urls import url, include

urlpatterns = [
    path("customer_insert",views.insertCustomer), 
    path("customer_update",views.updateCustomer),
    path("customer_delete",views.deleteCustomer), 
    path("customer_viewsingle",views.displayCustomer), 
    path("customer_viewall",views.displayAllCustomer), 
    path("home",views.homepage), 
]