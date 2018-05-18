from django.urls import path
from orders.views import OrderCreate, AdminOrderDetail


app_name='orders'

urlpatterns = [
    path('create/', OrderCreate, name='OrderCreate'),
    path('admin/order/<order_id>', AdminOrderDetail, name='AdminOrderDetail')
]