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
    path('product_details/<int:p_id>',views.user_product_details,name = 'product_details'),
    path('get_quantity/',views.get_quantity, name='get_quantity'),
    # path('profile',views.profile,name = 'profile'),
    path('personal_details',views.personal_details, name = 'personal_details'),
    path('edit_personal_details',views.edit_personal_details,name = 'edit_personal_details'),
    path('manage_address',views.manage_address, name = 'manage_address'),
    path('edit_manage_address',views.edit_manage_address, name = 'edit_manage_address'),
    path('coupon',views.my_coupons, name = 'coupon'),
    path('my_reviews',views.my_reviews,name = 'my_reviews'),
    path('cart',views.user_cart,name = 'cart'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('delete_from_cart/', views.delete_from_cart, name='delete_from_cart'),
    # path('checkout',views.checkout, name = 'checkout'),
    path('pdf',views.generate_pdf, name = 'pdf'),
    
]