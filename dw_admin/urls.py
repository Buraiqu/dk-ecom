from django.urls import path
from . import views
from .views import CSVView

app_name='dwadmin'
urlpatterns = [
    path('',views.index, name = 'index'),
    path('view_seller',views.view_seller,name= 'view_seller'),
    path('approve_seller',views.approve_seller,name= 'approve_seller'),
    path('btn_approve_seller/<int:sid>',views.btn_approve_seller,name='btn_approve_seller'),
    path('btn_reject_seller/<int:sid>',views.btn_reject_seller,name='btn_reject_seller'),
    path('view_user',views.view_user,name= 'view_user'),
    path('complaints',views.complaints,name= 'complaints'),
    path('csv/', CSVView.as_view(), name='csv'),
     # ... other URL patterns ...
]