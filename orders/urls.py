from django.urls import path
from orders.views import Order_Create, Admin_Order_Detail
from orders.views import Order_List_View
from orders.views import Order_Create_View

app_name='orders'

urlpatterns = [
    path('api/order-list', Order_List_View.as_view()),
    # path('api/order-create', Order_Create_View.as_view()),
    path('create/', Order_Create, name='OrderCreate'),
    path('admin/order/<order_id>', Admin_Order_Detail, name='AdminOrderDetail')
]