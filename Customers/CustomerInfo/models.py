from django.db import models
from uuid import uuid4

def generateUUID():
    return str(uuid4())

class record(models.Model):
    recordAdded = models.DateTimeField(auto_now_add=True)
    recordModified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class customer(record):
     customerId = models.CharField(primary_key=True, default=generateUUID, editable=False,max_length=200)
     firstName = models.CharField(max_length=200, blank=False, null=False)
     lastName = models.CharField(max_length=200, blank=False, null=False)
     address = models.CharField(max_length=200, blank=False, null=False)
     email = models.CharField(max_length=200, blank=False, null=False)
     mobileNo = models.CharField(max_length=15, blank=False, null=False)
     country = models.CharField(max_length=100, blank=False, null=False)

     def __str__(self):
         return str(self.customerId)
