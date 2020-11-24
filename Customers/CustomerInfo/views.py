from django.shortcuts import render
from CustomerInfo.models import customer
from django.contrib.auth.decorators import login_required

'''
To insert Customer records
'''
@login_required
def insertCustomer(request):
    user_group = list(request.user.groups.values_list('name',flat = True))
    
    if "Customer" in user_group:
        personalData = customer.objects.get(customerId=request.user)
        context = {"customer": personalData}
        return render(request, "my_record.htm",context)

    else:

        if request.method == 'POST':  
            if request.POST.get('firstName') and request.POST.get('lastName'):
                try:
                    data=customer()
                    data.firstName= request.POST.get('firstName')
                    data.lastName= request.POST.get('lastName')
                    data.email= request.POST.get('email')
                    data.mobileNo= request.POST.get('mobileNo')
                    data.address= request.POST.get('address')
                    data.country= request.POST.get('country')
                    data.save()
                        
                    context = {"customer": data}
                    return render(request, 'customer_insert.htm',context)

                except Exception as e:
                    print(str(e))
                    return render(request, 'customer_insert.htm')
            
            else:
                return render(request, 'customer_insert.htm') 

        else:
                return render(request,'customer_insert.htm')

'''
To update records
'''
@login_required
def updateCustomer(request):

    user_group = list(request.user.groups.values_list('name',flat = True))
    
    if "Customer" in user_group:
        personalData = customer.objects.get(customerId=request.user)
        context = {"customer": personalData}
        return render(request, "my_record.htm",context)

    else:
    
        if request.method == 'POST':  
            if request.POST.get('customerId'):

                try:
                    data = customer.objects.get(customerId=request.POST.get('customerId'))
                    if(data):

                        flag=0

                        for key in request.POST.keys():
        
                            if((key=='mobileNo') and request.POST.get('mobileNo')):
                                data.mobileNo= request.POST.get('mobileNo')
                                flag=1

                            if((key=='address') and request.POST.get('address')):
                                data.address= request.POST.get('address')
                                flag=1

                            if((key=='country') and request.POST.get('country')):
                                data.country= request.POST.get('country')
                                flag=1
                                
                        if(flag==1):
                            data.save()
                            
                        context = {"customer": data}
                        return render(request, 'customer_update.htm',context)
                    else:
                        return render(request, 'customer_update.htm') 
                

                except Exception as e:
                    print(str(e))
                    return render(request, 'customer_update.htm')
            
            else:
                return render(request, 'customer_update.htm') 

        else:
            return render(request,'customer_update.htm')

'''
To delete customer records
'''
@login_required
def deleteCustomer(request):

    user_group = list(request.user.groups.values_list('name',flat = True))
    
    if "Customer" in user_group:
        personalData = customer.objects.get(customerId=request.user)
        context = {"customer": personalData}
        return render(request, "my_record.htm",context)

    else:

        if request.method == 'POST':  
            if request.POST.get('customerId'):
                try:
                    data = customer.objects.get(customerId=request.POST.get('customerId'))

                    if(data):
                        data.delete()   
                        information={"value":"Successfully deleted the record"}  
                        context = {"message": information}
                        return render(request, 'customer_delete.htm',context)
                    else:
                        raise Exception("Customer ID not found")

                except Exception as e:
                    print(str(e))
                    information={"value":"Error occurred : "+str(e)}
                    context = {"message": information}
                    return render(request, 'customer_delete.htm',context)
            
            else:
                return render(request, 'customer_delete.htm') 

        else:
                return render(request,'customer_delete.htm')

'''
To display single customer record
'''
@login_required
def displayCustomer(request):

    user_group = list(request.user.groups.values_list('name',flat = True))
    
    if "Customer" in user_group:
        personalData = customer.objects.get(customerId=request.user)
        context = {"customer": personalData}
        return render(request, "my_record.htm",context)
    else:
        if request.method == 'POST':  
            if request.POST.get('customerId'):
                try:
                    data = customer.objects.get(customerId=request.POST.get('customerId'))

                    if(data):
                        context = {"customer": data}
                        return render(request, 'customer_viewsingle.htm',context)
                    else:
                        raise Exception("Customer ID not found")

                except Exception as e:
                    print(str(e))
                    return render(request, 'customer_viewsingle.htm')
            
            else:
                return render(request, 'customer_viewsingle.htm') 

        else:
                return render(request,'customer_viewsingle.htm')

'''
To display all customer records
'''
@login_required
def displayAllCustomer(request):

    user_group = list(request.user.groups.values_list('name',flat = True))
    
    if "Customer" in user_group:
        personalData = customer.objects.get(customerId=request.user)
        context = {"customer": personalData}
        return render(request, "my_record.htm",context)
    else:
        try:
            data = customer.objects.all()

            if(data):
                context = {"customer": data}
                return render(request, 'customer_viewall.htm',context)
            else:
                raise Exception("Customer records not found")

        except Exception as e:
            print(str(e))
            return render(request, 'customer_viewall.htm')


'''
To display home page
'''
@login_required
def homepage(request):

    user_group = list(request.user.groups.values_list('name',flat = True))
    
    if "Customer" in user_group:
        personalData = customer.objects.get(customerId=request.user)
        context = {"customer": personalData}
        return render(request, "my_record.htm",context)
    else:
        return render(request, "index.htm")
