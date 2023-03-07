from django.shortcuts import render
from home.models import Customer
# Create your views here.
def user(request):
    customer_details = Customer.objects.get(id = request.session['customer'])
    return render(request,'user_templates/user_index.html')

def user_jacket(request):
    return render(request,'user_templates/jacket.html')

def user_hoodie(request):
    return render(request,'user_templates/hoodie.html')

def user_sweater(request):
    return render(request,'user_templates/sweaters.html')

def user_tshirt(request):
    return render(request,'user_templates/t-shirt.html')

def user_pant(request):
    return render(request,'user_templates/pants.html')

def user_hats(request):
    return render(request,'user_templates/hats.html')                 

def user_accessories(request):
    return render(request,'user_templates/accessories.html') 

def user_product_details(request):
    return render(request,'user_templates/product_details.html')

def user_cart(request):
    return render(request,'user_templates/cart.html')