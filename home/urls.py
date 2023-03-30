from django.urls import path
from . import views

app_name='homepage'
urlpatterns = [
    path('',views.home_homepage,name = 'home'),
    path('seller_login',views.seller_login,name = 'seller_login'),
    path('seller_registration',views.seller_registration,name = 'seller_registration'),
    path('login',views.home_login,name = 'login'),
    path('register',views.home_register,name = 'register'),
    path('jacket',views.home_jacket,name = 'jacket'),
    path('hoodie',views.home_hoodie,name = 'hoodie'),
    path('sweater',views.home_sweater,name = 'sweater'),
    path('t-shirt',views.home_tshirt,name = 't-shirt'),
    path('pants',views.home_pant,name = 'pants'),
    path('hats',views.home_hats,name = 'hats'),
    path('jewelery',views.home_jewelery,name = 'jewelery'),
    path('accessories',views.home_accessories,name = 'accessories'),
    path('product_details',views.product_details,name = 'product_details')

]