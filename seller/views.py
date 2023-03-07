from django.shortcuts import render,redirect
from .models import Category,Fit,Material,Pattern,Neck,Sleeve,Size,Variant,Products,Album
from home.models import Seller
import pprint
import os
from django.contrib import messages


# Create your views here.
def seller_variant(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        quantities = request.POST.getlist("quantity[]")
        sizes = request.POST.getlist("size_id[]")
        print(product_id)
        print(quantities)

        for i in range(len(quantities)):
            variant = Variant(
                product_id_id=product_id,
                size_id_id=sizes[i],
                quantity=quantities[i]
            )
            variant.save()

        return redirect("seller:variant")
    products = Products.objects.all()
    size = Size.objects.all()
    return render(request,'seller_templates/add_product_variant.html',{'products':products,'sizes':size})


def view_variant(request,pid=0):
    variant = Variant.objects.filter(product_id = pid)
    return render(request,'seller_templates/view_variants.html',{'data':variant})


def product_list(request):
    products = Products.objects.all().values('id', 'product_name')
    return JsonResponse(list(products), safe=False)


def delete_product(request,pid=0):
    product = Products.objects.get(id = pid)
    if len(product.thumbnail)>0:
        os.remove(product.thumbnail.path) 
    product.delete()
    messages.success(request,"Product deleted successfully")
    return redirect("seller:viewproducts")
    return render(request,'seller_templates/seller_view.html')


def seller_home(request):
    sellers = Seller.objects.get(id = request.session['seller'])
    category = Category.objects.all()
    fit = Fit.objects.all()
    material = Material.objects.all()
    neck = Neck.objects.all()
    sleeve = Sleeve.objects.all()
    pattern = Pattern.objects.all()
    
    
    if request.method == 'POST':
        p_name = request.POST['productname']
        p_description = request.POST['description']
        p_category = Category.objects.get(id = request.POST['category'])
        p_price = request.POST['price']
        p_image = request.FILES['pic']
        seller = Seller.objects.get(id = request.session['seller'])
        p_material = Material.objects.get(id = request.POST['material'])
        p_fit = Fit.objects.get(id = request.POST['fittype'])
        p_sleeve = Sleeve.objects.get(id = request.POST['sleeve'])
        p_neck = Neck.objects.get(id = request.POST['neck'])
        p_pattern = Pattern.objects.get(id = request.POST['pattern'])
        p_album = request.FILES.getlist('files[]')
        

        p_product = Products(
            product_name= p_name,
            description=  p_description,
            category_id = p_category,
            price= p_price,
            thumbnail =  p_image,
            seller_id = seller,
            material_id = p_material,
            fit_id = p_fit,
            sleeve_id = p_sleeve,
            neck_id = p_neck,
            pattern_id = p_pattern
        )
        pprint.pprint(p_product)
        p_product.save()  
        product_id = p_product.id
        
        for i in p_album:
            album_p = Album(
                product_id = product_id,
                image = i 
            )
            album_p.save()
        
        
    context = {
        'categorys':category,
        'fits':fit,
        'materials':material,
        'necks':neck,
        'sleeves':sleeve,
        'patterns':pattern,
        'seller':sellers,
    }
    return render(request,'seller_templates/seller_index.html',context)


def seller_products(request):
    product_obj = Products.objects.filter(seller_id=request.session['seller'])
    return render(request,'seller_templates/seller_view.html',{'data':product_obj})

    
def seller_change_password(request):
    msg = ''
    if request.method == 'POST':
        old_pass = request.POST['old']
        new_pass = request.POST['confirm']
        try:
            seller_obj = Seller.objects.get(id = request.session['seller'],password = old_pass)
            Seller.objects.filter(id = request.session['seller']).update(password = new_pass)
            msg = 'Change Successfull'
            return render(request,'seller_templates/change_password.html',{'message1':msg})
        except:
            msg = 'old Password does not match' 
            return render(request,'seller_templates/change_password.html',{'message':msg})
    return render(request,'seller_templates/change_password.html')


def seller_update_stock(request):
    pro = Products.objects.filter(seller_id=request.session['seller'])
    context = {
        'product':pro
    }
    return render(request,'seller_templates/stock_update.html',context)


def seller_stock_up(request):
    id = request.POST['pno']
    prod = Products.objects.filter(id = id).values('product_name','Stock')
    protitle = prod[0]['product_name']
    prostock = prod[0]['Stock']
    print(protitle)
    context = {
        'product_name':protitle,
        'Stock':prostock,
    }
    
    return JsonResponse(context)
    return render(request,'seller_templates/stock_update.html')


def seller_add_stock(request):
    new_stock =request.POST['new_stock']
    pno = request.POST['pno']
    prod = Products.objects.get(id = pno)
    pro = prod.Stock
    pro = pro +int(new_stock)
    Products.objects.filter(id= pno).update(Stock=pro)
    msg = 'Updated Successfully'
    context = {
        'message':msg,
    }
    return JsonResponse(context)    


def seller_profile(request):
    return render(request,'seller_templates/profile.html')