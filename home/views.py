from django.shortcuts import render,redirect
from home.models import Customer
from home.models import Seller
from django.contrib import messages
from django.shortcuts import render 
from django.http import HttpResponse 
import logging
from random import randint
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def home_homepage(request):
    return render(request,'home_templates/user_index.html')
    

def home_login(request):
    msg="" 
    if request.method == 'POST':
        u_email = request.POST['email']  
        u_password = request.POST['password']
        try:
            customerlog = Customer.objects.get(
                email= u_email,
                password= u_password
            )
            request.session['customer'] = customerlog.id
            return redirect('user:home')
        except:
              msg="Invalid Username or password"  
            #   return redirect('common:user_form') 
    return render(request,'home_templates/login1.html',{'message':msg}) 

def home_register(request):
    if request.method == 'POST':
        print('test')
        u_name = request.POST['name']
        u_gender = request.POST['gender']
        u_phone = request.POST['phone']
        u_dob = request.POST['dob']
        u_house = request.POST['house']
        u_street = request.POST['street']
        u_city = request.POST['city']
        u_pincode = request.POST['pincode']
        u_email = request.POST['email']
        u_password = request.POST['password']
        u_customer = Customer(
            name= u_name,
            gender= u_gender,
            phone= u_phone,
            dob= u_dob,
            house= u_house,
            street= u_street,
            city= u_city,
            pincode= u_pincode,
            email= u_email,
            password= u_password
        )
        u_customer.save()  
        messages.success( request,'Successfully Registered')
        return redirect('homepage:login')
    return render(request,'home_templates/register.html')

def seller_login(request):
    msg="" 
    if request.method == 'POST':
        s_username= request.POST['username']  
        s_password = request.POST['password']
        try:
            sellerlog = Seller.objects.get(username= s_username,password= s_password)
            request.session['seller'] = sellerlog.id
            return redirect('seller:shome')
        except:
            msg="Invalid Username or password"  
            #return redirect('common:user_form') 
    return render(request,'home_templates/seller_login.html',{'message':msg})

def seller_registration(request):
     if request.method == 'POST':
        s_name = request.POST['name']
        s_username = request.POST['username']
        s_email = request.POST['email']
        s_phone = request.POST['phone']
        s_account = request.POST['account']
        s_ifsc = request.POST['ifsc']
        s_adddress = request.POST['address']
        s_sellerpic = request.FILES['sellerpic']
        s_password = str(s_username)+'-'+s_phone[6-10]
        s_seller = Seller(
            name= s_name,
            username=s_username,
            email= s_email,
            phone= s_phone,
            address= s_adddress,
            account=s_account,
            ifsc= s_ifsc,
            password= s_password,
            sellerpic= s_sellerpic  
        )
        s_seller.save()     
        messages.success( request,'Successfully Registered')
        email_subject='DarkWear Seller Account Registration'
        email_content='Dear team '+str(s_username)+'\n Thank You for registering your buisness with our website.\nWe ar eager to do buisness with you and grow our business higher together.\nYour password for login is\n password:'+s_password
         
        send_mail(
                  email_subject,
                  email_content, 
                  settings.EMAIL_HOST_USER,
                  [s_email,])
        return redirect('homepage:seller_login')
     return render(request,'home_templates/seller_registration.html')

def home_jacket(request):
    return render(request,'home_templates/jacket.html')

def home_hoodie(request):
    return render(request,'home_templates/hoodie.html')

def home_sweater(request):
    return render(request,'home_templates/sweaters.html')

def home_tshirt(request):
    return render(request,'home_templates/t-shirt.html')

def home_pant(request):
    return render(request,'home_templates/pants.html')

def home_hats(request):
    return render(request,'home_templates/hats.html')                 

def home_accessories(request):
    return render(request,'home_templates/accessories.html')

def home_jewelery(request):
    return render(request,'home_templates/jewelery.html')                   

def product_details(request):
    return render(request,'user_templates/product_details.html')