from django.urls import path
from . import views


app_name='seller'
urlpatterns = [
    path('',views.seller_home,name = 'shome'),
    path('viewproducts',views.seller_products,name = 'viewproducts'),
    path('btn_approve_product/<int:pid>',views.btn_approve_product,name='btn_approve_product'),
    path('btn_reject_product/<int:pid>',views.btn_reject_product,name='btn_reject_product'),
    path('view_details/<int:pid>',views.view_details,name = 'view_details'),
    path('view_approved_products',views.seller_approved_products,name = 'view_approved_products'),
    path('product_variant',views.seller_variant,name = 'variant'),
    path('view_variant/<int:pid>',views.view_variant,name = 'view_variant'),
    path('delete_product/<int:pid>',views.delete_product,name = 'delete_product'),
    path('product_list',views.product_list, name='product_list'),
    path('changepassword',views.seller_change_password,name = 'changepassword'),
    path('stockupdate',views.seller_update_stock,name = 'stockupdate'),
    path('get_product_name/', views.get_product_name, name='get_product_name'),
    path('get_variant/',views.get_variant, name = 'get_variant'),
    path('get_size/',views.get_size,name = 'get_size'),
    path('stock_up',views.seller_stock_up,name = 'stock_up'),
    path('add_stock',views.seller_add_stock,name = 'add_stock'),
    path('profile',views.seller_profile,name = 'profile'),
    path('edit_approved_products/<int:pid>',views.edit_approved_products,name = "edit_approved_products")
]           