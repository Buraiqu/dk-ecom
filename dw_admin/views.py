from django.shortcuts import render,redirect
from home.models import Seller
from home.models import Customer

# Create your views here.
def index(request):
    return render(request,'admin_templates/admin_index.html')

def view_seller(request):
    seller = Seller.objects.filter(status = 'approved')
    return render(request,'admin_templates/view_seller.html')

def approve_seller(request):
    seller = Seller.objects.filter(status = 'pending')
    return render(request,'admin_templates/approve_seller.html',{'seller':seller})

def btn_approve_seller(request,sid):
    seller = Seller.objects.filter(id = sid).update(status='approved')
    # user_name=seller.user_name
    # pwd=seller.password
    # email_subject='account user name and password'
    # email_content='user name :'+str(user_name) + 'password' + pwd
    # send_mail(
    #     email_subject,
    #     email_content,
    #     settings.EMAIL_HOST_USER,
    #     [email,]  
    # )
    return redirect('dwadmin:approve_seller')


def btn_reject_seller(request,sid):
    seller = Seller.objects.filter(id = sid).delete(status='pending')
    return redirect('dwadmin:approve_seller')

def view_user(request):
    customer = Customer.objects.all()
    return render(request,'admin_templates/view_user.html')

def complaints(request):
    return render(request,'admin_templates/complaints.html')

