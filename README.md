# CustomerDetails-App
This is a sample Django App which is used to store Customer Details (Refer Master Branch)


This App has 2 Views for Admin and Customer
------------------------------------------------
Admin view supports Adding, Deleting, Updating, Viewing Single and All Customer records
Customer view supports only viewing their individual record

How to Run it after cloning this App
----------------------------------------
1. Create Virtual Environment and Activate it
virtualenv myvirtual
myvirtual/scripts/activate

2. Install the packages using requirements.txt in the App
pip install -r .\requirements.txt

3. python .\manage.py makemigrations

4. python .\manage.py migrate

5. python .\manage.py createsuperuser (To create SuperUser Account)

6. python .\manage.py runserver

7. Log into Django Admin using superuser account -> Create a Group called "Customer"
Address - http://127.0.0.1:8000/Admin

8. Log into Application (Admin View) via superuser account created above
Address - http://127.0.0.1:8000/home

9. Log in Application (Customer View) using CustomerID created and the Password "Customer@123"
Address - http://127.0.0.1:8000/home

Developer - K.Janarthanan
