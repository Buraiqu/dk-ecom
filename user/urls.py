from django.urls import path
from . import views
app_name='user'
urlpatterns = [
    path('',views.user,name='home'),
     path('jacket',views.user_jacket,name = 'jacket'),
    path('hoodie',views.user_hoodie,name = 'hoodie'),
    path('sweater',views.user_sweater,name = 'sweater'),
    path('t-shirt',views.user_tshirt,name = 't-shirt'),
    path('pants',views.user_pant,name = 'pants'),
    path('hats',views.user_hats,name = 'hats'),
    path('accessories',views.user_accessories,name = 'accessories'),
    path('product_details',views.user_product_details,name = 'product_details'),
    path('cart',views.user_cart,name = 'cart')
]