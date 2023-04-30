from django.shortcuts import render,redirect
from home.models import *
from seller.models import *
from user.models import *
from home.models import *
import pprint
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Cart



# Create your views here.
# def profile(request):
#     return render(request,'user_templates/profile.html',{'customer':customer})

def personal_details(request):
    customer = Customer.objects.get(id = request.session['customer'])
    return render(request,'user_templates/profile-personal-details.html',{'customer':customer})

def edit_personal_details(request):
    customer = Customer.objects.get(id=request.session['customer'])
    if request.method == 'POST':
        customer.name = request.POST['name']
        customer.email = request.POST['email']
        customer.phone = request.POST['phone']
        customer.dob = request.POST['dob']
        customer.save()
        return redirect('user:personal_details')
    return render(request,'user_templates/profile-edit-personal-details.html',{'customer':customer})

def manage_address(request):
    customer = Customer.objects.get(id = request.session['customer'])
    return render(request,'user_templates/profile-manage-address.html',{'customer':customer})

def edit_manage_address(request):
    customer = Customer.objects.get(id=request.session['customer'])
    if request.method == 'POST':
        customer.house = request.POST['house']
        customer.street = request.POST['street']
        customer.city = request.POST['city']
        customer.pincode = request.POST['pincode']
        customer.save()
        return redirect('user:manage_address')
    return render(request,'user_templates/profile-edit-manage-address.html',{'customer':customer})

def my_coupons(request):
    customer = Customer.objects.get(id = request.session['customer'])
    return render(request,'user_templates/profile-coupon.html',{'customer':customer})

def my_reviews(request):
    customer = Customer.objects.get(id = request.session['customer'])
    return render(request,'user_templates/profile-my-reviews.html',{'customer':customer})

def user(request):
    customer_details = Customer.objects.get(id = request.session['customer'])
    return render(request,'user_templates/user_index.html')

def user_jacket(request):
    category = Category.objects.get(category_name = 'jacket')
    jacket = Products.objects.filter(category_id = category,status = 'approved')
    
    pprint.pprint(jacket)
    return render(request,'user_templates/jacket.html',{'jackets':jacket})


def user_hoodie(request):
    category = Category.objects.get(category_name = 'hoodie')
    hoodie = Products.objects.filter(category_id = category,status = 'approved')
    return render(request,'user_templates/hoodie.html',{'hoodies':hoodie})

def user_sweater(request):
    category = Category.objects.get(category_name = 'sweatshirt')
    sweater = Products.objects.filter(category_id = category,status = 'approved')
    return render(request,'user_templates/sweaters.html',{'sweaters':sweater})

def user_tshirt(request):
    category = Category.objects.get(category_name = 't-shirt')
    tshirt = Products.objects.filter(category_id = category,status = 'approved')
    return render(request,'user_templates/t-shirt.html',{'tshirts':tshirt})

def user_pant(request):
    category = Category.objects.get(category_name = 'pant')
    pant = Products.objects.filter(category_id = category,status = 'approved')
    return render(request,'user_templates/pants.html',{'pants':pant})

def user_hats(request):
    category = Category.objects.get(category_name = 'hat')
    hat = Products.objects.filter(category_id = category,status = 'approved')
    return render(request,'user_templates/hats.html',{'hats':hat})                 

def user_accessories(request):
    category = Category.objects.get(category_name = 'accessories')
    accessory = Products.objects.filter(category_id = category,status = 'approved')
    return render(request,'user_templates/accessories.html',{'accessories':accessory}) 

def user_product_details(request, p_id):
    print(request)
    msg="" 
    product = Products.objects.get(id = p_id)
    variants = Variant.objects.filter(product_id = p_id)
    print(variants)
    album = Album.objects.filter(product_id = p_id)
    
    show_fit_type = True
    show_size_guide = True
    if product.category_id.category_name in ['accessories', 'hat']:
        show_fit_type = False
        try:
            context = {
                'product': product,
                'variants': variants,
                'albums': album,
                'show_fit_type': show_fit_type,
                'show_size_guide': show_size_guide,
                'size_guide': product.size_guide.url
            }
        except ValueError:
            show_size_guide = False
            context = {
                'product': product,
                'variants': variants,
                'albums': album,
                'show_fit_type': show_fit_type,
                'show_size_guide': show_size_guide,
                'size_guide': None  # default value for size_guide
            }

    else:
        context = {
            'product': product,
            'variants': variants,
            'albums': album,
            'show_fit_type': show_fit_type,
            'show_size_guide': show_size_guide,
            'size_guide': product.size_guide.url
        }
        
    if request.method == 'POST':
        u_id=request.session.get('customer')
        quantity = request.POST.get('quantity')
        # v_id = request.POST.get('variant_id')
        # print(v_id)
        size = request.POST.get('size')
        size_id = size_id = int(size.split()[2].strip("()"))
        print(size_id)
        variants = Variant.objects.get(product_id = product,size_id=size_id)
        print(variants)
        item = Cart.objects.filter(customer_id =u_id ,product_id = p_id,variant_id=variants.id).exists()
        print(item)
        if not item:           #same as if item == false:
            cart= Cart(customer_id =u_id,product_id = p_id,variant_id=variants.id,qty = quantity)
            cart.save()
            return redirect('user:cart')

        else:
            print('already in cart')
            msg = 'Item already in cart'
            
        
    return render(request,'user_templates/product_details.html',context)

def get_quantity(request):
    print(request)
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        size_id = request.GET.get('size_id')
        print(size_id)
        print(product_id,size_id)
    variant = Variant.objects.get(product_id=product_id, size_id=size_id)
    available_quantity = variant.quantity

    data = {
        'available_quantity': available_quantity,
    }

    return JsonResponse(data)


    

def user_cart(request):
    if request.method == 'POST':
        return redirect('user:pdf') 
    cart = Cart.objects.filter(customer_id=request.session['customer'])
    product_id=Products.objects.all()     
    return render(request,'user_templates/cart.html',{'items':cart})

def update_cart(request):
    if request.method == 'POST':
        cart_item_id = request.POST.get('cart_item_id')
        quantity = request.POST.get('quantity')
        cart_item = Cart.objects.get(id=cart_item_id)
        cart_item.qty = quantity
        cart_item.save()
        cart = Cart.objects.filter(customer_id=request.session['customer'])
        cart_html = render_to_string('cart.html', {'items': cart})
        messages.success(request, "Cart updated successfully")
        return HttpResponse(cart_html)
    else:
        return redirect('cart')

@csrf_exempt
def delete_from_cart(request):
    if request.method == 'POST':
        cart_item_id = request.POST.get('cart_item_id')
        try:
            cart_item = Cart.objects.get(id=cart_item_id)
            cart_item.delete()
            return JsonResponse({'success': True})
        except Cart.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Cart item does not exist.'})
    else:
         return JsonResponse({'success': False, 'error': 'Invalid request method.'})
     

# def checkout(request):
#     customer = Customer.objects.get(id = request.session['customer'])
#     items = Cart.objects.filter(customer_id=request.session['customer'])
#     grand_total = 0
#     for item in items:
#         grand_total += item.product.price * item.qty
    
#     context = {
#         'items': items,
#         'grand_total': grand_total,
#         'customers' : customer,
#     }
    
#     return render(request, 'user_templates/checkout.html', context)

def generate_pdf(request):
    customer = Customer.objects.get(id = request.session['customer'])
    items = Cart.objects.filter(customer_id=request.session['customer'])
    grand_total = 0
    for item in items:
        grand_total += item.product.price * item.qty
    
    context = {
        'items': items,
        'grand_total': grand_total,
        'customers' : customer,
    }
    
    template_path = 'user_templates/checkout.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="checkout.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('An error occurred while generating the PDF')
    
    return response     
     