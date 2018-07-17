from django.urls import path
from orders.views import Order_Create, Admin_Order_Detail


app_name='orders'

urlpatterns = [
    path('create/', Order_Create, name='OrderCreate'),
    path('admin/order/<order_id>', Admin_Order_Detail, name='AdminOrderDetail')
]