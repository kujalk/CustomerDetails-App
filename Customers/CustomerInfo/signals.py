from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.backends.signals import connection_created
from .models import customer

@receiver(post_save,sender=customer)
def new_user_registration(sender, instance, created,**kwargs):
    if created:
        print("new customer is created, therefore going to register it in Auth Model")
        
        #Filter customer object to get more attributes
        newCustomer=customer.objects.get(customerId=instance)

        #Add the user to Auth.models.User Table
        user = User.objects.create_user(username=instance,email=newCustomer.email,password='Customer@123',
        first_name=newCustomer.firstName,last_name=newCustomer.lastName)

        #Add the user to new group
        customergroup = Group.objects.get(name='Customer') 
        customergroup.user_set.add(user)